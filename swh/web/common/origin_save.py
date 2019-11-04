# Copyright (C) 2018-2019  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU Affero General Public License version 3, or any later version
# See top-level LICENSE file for more information

import json
import logging

from bisect import bisect_right
from datetime import datetime, timezone, timedelta

import requests

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.html import escape

from swh.web import config
from swh.web.common import service
from swh.web.common.exc import BadInputExc, ForbiddenExc, NotFoundExc
from swh.web.common.models import (
    SaveUnauthorizedOrigin, SaveAuthorizedOrigin, SaveOriginRequest,
    SAVE_REQUEST_ACCEPTED, SAVE_REQUEST_REJECTED, SAVE_REQUEST_PENDING,
    SAVE_TASK_NOT_YET_SCHEDULED, SAVE_TASK_SCHEDULED,
    SAVE_TASK_SUCCEED, SAVE_TASK_FAILED, SAVE_TASK_RUNNING
)
from swh.web.common.origin_visits import get_origin_visits
from swh.web.common.utils import parse_timestamp

from swh.scheduler.utils import create_oneshot_task_dict

scheduler = config.scheduler()

logger = logging.getLogger(__name__)


def get_origin_save_authorized_urls():
    """
    Get the list of origin url prefixes authorized to be
    immediately loaded into the archive (whitelist).

    Returns:
        list: The list of authorized origin url prefix
    """
    return [origin.url
            for origin in SaveAuthorizedOrigin.objects.all()]


def get_origin_save_unauthorized_urls():
    """
    Get the list of origin url prefixes forbidden to be
    loaded into the archive (blacklist).

    Returns:
        list: the list of unauthorized origin url prefix
    """
    return [origin.url
            for origin in SaveUnauthorizedOrigin.objects.all()]


def can_save_origin(origin_url):
    """
    Check if a software origin can be saved into the archive.

    Based on the origin url, the save request will be either:

      * immediately accepted if the url is whitelisted
      * rejected if the url is blacklisted
      * put in pending state for manual review otherwise

    Args:
        origin_url (str): the software origin url to check

    Returns:
        str: the origin save request status, either **accepted**,
        **rejected** or **pending**
    """
    # origin url may be blacklisted
    for url_prefix in get_origin_save_unauthorized_urls():
        if origin_url.startswith(url_prefix):
            return SAVE_REQUEST_REJECTED

    # if the origin url is in the white list, it can be immediately saved
    for url_prefix in get_origin_save_authorized_urls():
        if origin_url.startswith(url_prefix):
            return SAVE_REQUEST_ACCEPTED

    # otherwise, the origin url needs to be manually verified
    return SAVE_REQUEST_PENDING


# map visit type to scheduler task
# TODO: do not hardcode the task name here (T1157)
_visit_type_task = {
    'git': 'load-git',
    'hg': 'load-hg',
    'svn': 'load-svn'
}


# map scheduler task status to origin save status
_save_task_status = {
    'next_run_not_scheduled': SAVE_TASK_NOT_YET_SCHEDULED,
    'next_run_scheduled': SAVE_TASK_SCHEDULED,
    'completed': SAVE_TASK_SUCCEED,
    'disabled': SAVE_TASK_FAILED
}


def get_savable_visit_types():
    return sorted(list(_visit_type_task.keys()))


def _check_visit_type_savable(visit_type):
    """
    Get the list of visit types that can be performed
    through a save request.

    Returns:
        list: the list of saveable visit types
    """
    allowed_visit_types = ', '.join(get_savable_visit_types())
    if visit_type not in _visit_type_task:
        raise BadInputExc('Visit of type %s can not be saved! '
                          'Allowed types are the following: %s' %
                          (visit_type, allowed_visit_types))


_validate_url = URLValidator(schemes=['http', 'https', 'svn', 'git'])


def _check_origin_url_valid(origin_url):
    try:
        _validate_url(origin_url)
    except ValidationError:
        raise BadInputExc('The provided origin url (%s) is not valid!' %
                          escape(origin_url))


def _get_visit_info_for_save_request(save_request):
    visit_date = None
    visit_status = None
    try:
        origin = {'url': save_request.origin_url}
        origin_info = service.lookup_origin(origin)
        origin_visits = get_origin_visits(origin_info)
        visit_dates = [parse_timestamp(v['date'])
                       for v in origin_visits]
        i = bisect_right(visit_dates, save_request.request_date)
        if i != len(visit_dates):
            visit_date = visit_dates[i]
            visit_status = origin_visits[i]['status']
            if origin_visits[i]['status'] == 'ongoing':
                visit_date = None
    except Exception:
        pass
    return visit_date, visit_status


def _check_visit_update_status(save_request, save_task_status):
    visit_date, visit_status = _get_visit_info_for_save_request(save_request)
    save_request.visit_date = visit_date
    # visit has been performed, mark the saving task as succeed
    if visit_date and visit_status is not None:
        save_task_status = SAVE_TASK_SUCCEED
    elif visit_status == 'ongoing':
        save_task_status = SAVE_TASK_RUNNING
    else:
        time_now = datetime.now(tz=timezone.utc)
        time_delta = time_now - save_request.request_date
        # consider the task as failed if it is still in scheduled state
        # 30 days after its submission
        if time_delta.days > 30:
            save_task_status = SAVE_TASK_FAILED
    return visit_date, save_task_status


def _save_request_dict(save_request, task=None):
    must_save = False
    visit_date = save_request.visit_date
    # save task still in scheduler db
    if task:
        save_task_status = _save_task_status[task['status']]
        # Consider request from which a visit date has already been found
        # as succeeded to avoid retrieving it again
        if save_task_status == SAVE_TASK_SCHEDULED and visit_date:
            save_task_status = SAVE_TASK_SUCCEED
        if save_task_status in (SAVE_TASK_FAILED, SAVE_TASK_SUCCEED) \
                and not visit_date:
            visit_date, _ = _get_visit_info_for_save_request(save_request)
            save_request.visit_date = visit_date
            must_save = True
        # Check tasks still marked as scheduled / not yet scheduled
        if save_task_status in (SAVE_TASK_SCHEDULED,
                                SAVE_TASK_NOT_YET_SCHEDULED):
            visit_date, save_task_status = _check_visit_update_status(
                save_request, save_task_status)

    # save task may have been archived
    else:
        save_task_status = save_request.loading_task_status
        if save_task_status in (SAVE_TASK_SCHEDULED,
                                SAVE_TASK_NOT_YET_SCHEDULED):
            visit_date, save_task_status = _check_visit_update_status(
                save_request, save_task_status)

        else:
            save_task_status = save_request.loading_task_status

    if save_request.loading_task_status != save_task_status:
        save_request.loading_task_status = save_task_status
        must_save = True

    if must_save:
        save_request.save()

    return {'id': save_request.id,
            'visit_type': save_request.visit_type,
            'origin_url': save_request.origin_url,
            'save_request_date': save_request.request_date.isoformat(),
            'save_request_status': save_request.status,
            'save_task_status': save_task_status,
            'visit_date': visit_date.isoformat() if visit_date else None}


def create_save_origin_request(visit_type, origin_url):
    """
    Create a loading task to save a software origin into the archive.

    This function aims to create a software origin loading task
    trough the use of the swh-scheduler component.

    First, some checks are performed to see if the visit type and origin
    url are valid but also if the the save request can be accepted.
    If those checks passed, the loading task is then created.
    Otherwise, the save request is put in pending or rejected state.

    All the submitted save requests are logged into the swh-web
    database to keep track of them.

    Args:
        visit_type (str): the type of visit to perform (currently only
            ``git`` but ``svn`` and ``hg`` will soon be available)
        origin_url (str): the url of the origin to save

    Raises:
        BadInputExc: the visit type or origin url is invalid
        ForbiddenExc: the provided origin url is blacklisted

    Returns:
        dict: A dict describing the save request with the following keys:

            * **visit_type**: the type of visit to perform
            * **origin_url**: the url of the origin
            * **save_request_date**: the date the request was submitted
            * **save_request_status**: the request status, either **accepted**,
              **rejected** or **pending**
            * **save_task_status**: the origin loading task status, either
              **not created**, **not yet scheduled**, **scheduled**,
              **succeed** or **failed**


    """
    _check_visit_type_savable(visit_type)
    _check_origin_url_valid(origin_url)
    save_request_status = can_save_origin(origin_url)
    task = None

    # if the origin save request is accepted, create a scheduler
    # task to load it into the archive
    if save_request_status == SAVE_REQUEST_ACCEPTED:
        # create a task with high priority
        kwargs = {'priority': 'high'}
        # set task parameters according to the visit type
        if visit_type == 'git':
            kwargs['repo_url'] = origin_url
        elif visit_type == 'hg':
            kwargs['origin_url'] = origin_url
        elif visit_type == 'svn':
            kwargs['origin_url'] = origin_url
            kwargs['svn_url'] = origin_url

        sor = None
        # get list of previously sumitted save requests
        current_sors = \
            list(SaveOriginRequest.objects.filter(visit_type=visit_type,
                                                  origin_url=origin_url))

        can_create_task = False
        # if no save requests previously submitted, create the scheduler task
        if not current_sors:
            can_create_task = True
        else:
            # get the latest submitted save request
            sor = current_sors[0]
            # if it was in pending state, we need to create the scheduler task
            # and update the save request info in the database
            if sor.status == SAVE_REQUEST_PENDING:
                can_create_task = True
            # a task has already been created to load the origin
            elif sor.loading_task_id != -1:
                # get the scheduler task and its status
                tasks = scheduler.get_tasks([sor.loading_task_id])
                task = tasks[0] if tasks else None
                task_status = _save_request_dict(sor, task)['save_task_status']
                # create a new scheduler task only if the previous one has been
                # already executed
                if task_status == SAVE_TASK_FAILED or \
                   task_status == SAVE_TASK_SUCCEED:
                    can_create_task = True
                    sor = None
                else:
                    can_create_task = False

        if can_create_task:
            # effectively create the scheduler task
            task_dict = create_oneshot_task_dict(
                _visit_type_task[visit_type], **kwargs)
            task = scheduler.create_tasks([task_dict])[0]

            # pending save request has been accepted
            if sor:
                sor.status = SAVE_REQUEST_ACCEPTED
                sor.loading_task_id = task['id']
                sor.save()
            else:
                sor = SaveOriginRequest.objects.create(visit_type=visit_type,
                                                       origin_url=origin_url,
                                                       status=save_request_status, # noqa
                                                       loading_task_id=task['id']) # noqa
    # save request must be manually reviewed for acceptation
    elif save_request_status == SAVE_REQUEST_PENDING:
        # check if there is already such a save request already submitted,
        # no need to add it to the database in that case
        try:
            sor = SaveOriginRequest.objects.get(visit_type=visit_type,
                                                origin_url=origin_url,
                                                status=save_request_status)
        # if not add it to the database
        except ObjectDoesNotExist:
            sor = SaveOriginRequest.objects.create(visit_type=visit_type,
                                                   origin_url=origin_url,
                                                   status=save_request_status)
    # origin can not be saved as its url is blacklisted,
    # log the request to the database anyway
    else:
        sor = SaveOriginRequest.objects.create(visit_type=visit_type,
                                               origin_url=origin_url,
                                               status=save_request_status)

    if save_request_status == SAVE_REQUEST_REJECTED:
        raise ForbiddenExc('The origin url is blacklisted and will not be '
                           'loaded into the archive.')

    return _save_request_dict(sor, task)


def get_save_origin_requests_from_queryset(requests_queryset):
    """
    Get all save requests from a SaveOriginRequest queryset.

    Args:
        requests_queryset (django.db.models.QuerySet): input
            SaveOriginRequest queryset

    Returns:
        list: A list of save origin requests dict as described in
        :func:`swh.web.common.origin_save.create_save_origin_request`
    """
    task_ids = []
    for sor in requests_queryset:
        task_ids.append(sor.loading_task_id)
    save_requests = []
    if task_ids:
        tasks = scheduler.get_tasks(task_ids)
        tasks = {task['id']: task for task in tasks}
        for sor in requests_queryset:
            sr_dict = _save_request_dict(sor, tasks.get(sor.loading_task_id))
            save_requests.append(sr_dict)
    return save_requests


def get_save_origin_requests(visit_type, origin_url):
    """
    Get all save requests for a given software origin.

    Args:
        visit_type (str): the type of visit
        origin_url (str): the url of the origin

    Raises:
        BadInputExc: the visit type or origin url is invalid
        NotFoundExc: no save requests can be found for the given origin

    Returns:
        list: A list of save origin requests dict as described in
        :func:`swh.web.common.origin_save.create_save_origin_request`
    """
    _check_visit_type_savable(visit_type)
    _check_origin_url_valid(origin_url)
    sors = SaveOriginRequest.objects.filter(visit_type=visit_type,
                                            origin_url=origin_url)
    if sors.count() == 0:
        raise NotFoundExc(('No save requests found for visit of type '
                           '%s on origin with url %s.')
                          % (visit_type, origin_url))
    return get_save_origin_requests_from_queryset(sors)


def get_save_origin_task_info(save_request_id):
    """
    Get detailed information about an accepted save origin request
    and its associated loading task.

    If the associated loading task info is archived and removed
    from the scheduler database, returns an empty dictionary.

    Args:
        save_request_id (int): identifier of a save origin request

    Returns:
        dict: A dictionary with the following keys:
            - **type**: loading task type
            - **arguments**: loading task arguments
            - **id**: loading task database identifier
            - **backend_id**: loading task celery identifier
            - **scheduled**: loading task scheduling date
            - **ended**: loading task termination date
            - **status**: loading task execution status
        Depending on the availability of the task logs in the elasticsearch
        cluster of Software Heritage, the returned dictionary may also
        contain the following keys:
            - **name**: associated celery task name
            - **message**: relevant log message from task execution
            - **duration**: task execution time (only if it succeeded)
            - **worker**: name of the worker that executed the task
    """
    try:
        save_request = SaveOriginRequest.objects.get(id=save_request_id)
    except ObjectDoesNotExist:
        return {}

    task = scheduler.get_tasks([save_request.loading_task_id])
    task = task[0] if task else None
    if task is None:
        return {}

    task_run = scheduler.get_task_runs([task['id']])
    task_run = task_run[0] if task_run else None
    if task_run is None:
        return {}
    task_run['type'] = task['type']
    task_run['arguments'] = task['arguments']
    task_run['id'] = task_run['task']
    del task_run['task']
    del task_run['metadata']
    del task_run['started']

    es_workers_index_url = config.get_config()['es_workers_index_url']
    if not es_workers_index_url:
        return task_run
    es_workers_index_url += '/_search'

    if save_request.visit_date:
        min_ts = save_request.visit_date
        max_ts = min_ts + timedelta(days=7)
    else:
        min_ts = save_request.request_date
        max_ts = min_ts + timedelta(days=30)
    min_ts = int(min_ts.timestamp()) * 1000
    max_ts = int(max_ts.timestamp()) * 1000

    save_task_status = _save_task_status[task['status']]
    priority = '3' if save_task_status == SAVE_TASK_FAILED else '6'

    query = {
        'bool': {
            'must': [
                {
                    'match_phrase': {
                        'priority': {
                            'query': priority
                        }
                    }
                },
                {
                    'match_phrase': {
                        'swh_task_id': {
                            'query': task_run['backend_id']
                        }
                    }
                },
                {
                    'range': {
                        '@timestamp': {
                            'gte': min_ts,
                            'lte': max_ts,
                            'format': 'epoch_millis'
                        }
                    }
                }
            ]
        }
    }

    try:
        response = requests.post(es_workers_index_url,
                                 json={'query': query,
                                       'sort': ['@timestamp']},
                                 timeout=30)
        results = json.loads(response.text)
        if results['hits']['total'] >= 1:
            task_run_info = results['hits']['hits'][-1]['_source']
            if 'swh_logging_args_runtime' in task_run_info:
                duration = task_run_info['swh_logging_args_runtime']
                task_run['duration'] = duration
            if 'message' in task_run_info:
                task_run['message'] = task_run_info['message']
            if 'swh_logging_args_name' in task_run_info:
                task_run['name'] = task_run_info['swh_logging_args_name']
            elif 'swh_task_name' in task_run_info:
                task_run['name'] = task_run_info['swh_task_name']
            if 'hostname' in task_run_info:
                task_run['worker'] = task_run_info['hostname']
            elif 'host' in task_run_info:
                task_run['worker'] = task_run_info['host']
    except Exception as e:
        logger.warning('Request to Elasticsearch failed\n%s' % str(e))
        pass

    return task_run
