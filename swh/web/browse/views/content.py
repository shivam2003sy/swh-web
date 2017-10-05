# Copyright (C) 2017  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from django.http import HttpResponse

from django.shortcuts import render

from swh.model.hashutil import hash_to_hex

from swh.web.common import query
from swh.web.common.utils import reverse
from swh.web.common.exc import handle_view_exception
from swh.web.browse.utils import (
    gen_path_info, request_content,
    prepare_content_for_display
)


def content_display(request, query_string):
    """Django view that produces an HTML display of a SWH content identified
    by its hash value.

    The url that points to it is :http:get:`/browse/content/[(algo_hash):](hash)/`

    Args:
        request: input django http request
        query_string: a string of the form "[ALGO_HASH:]HASH" where
            optional ALGO_HASH can be either *sha1*, *sha1_git*, *sha256*,
            or *blake2s256* (default to *sha1*) and HASH the hexadecimal
            representation of the hash value

    Returns:
        The HTML rendering of the requested content.

    """ # noqa
    try:
        algo, checksum = query.parse_hash(query_string)
        checksum = hash_to_hex(checksum)
        content_data, mime_type = request_content(query_string)
    except Exception as exc:
        return handle_view_exception(exc)

    path = request.GET.get('path', None)

    content_display_data = prepare_content_for_display(content_data,
                                                       mime_type, path)

    root_dir = None
    filename = None
    path_info = None

    breadcrumbs = []

    if path:
        split_path = path.split('/')
        root_dir = split_path[0]
        filename = split_path[-1]
        path = path.replace(root_dir + '/', '')
        path = path.replace(filename, '')
        path_info = gen_path_info(path)
        breadcrumbs.append({'name': root_dir[:7],
                            'url': reverse('browse-directory',
                                           kwargs={'sha1_git': root_dir})})
        for pi in path_info:
            breadcrumbs.append({'name': pi['name'],
                                'url': reverse('browse-directory',
                                               kwargs={'sha1_git': root_dir,
                                                       'path': pi['path']})})
        breadcrumbs.append({'name': filename,
                            'url': None})

    query_params = None
    if filename:
        query_params = {'filename': filename}

    content_raw_url = reverse('browse-content-raw',
                              kwargs={'query_string': query_string},
                              query_params=query_params)

    return render(request, 'content.html',
                  {'content_hash_algo': algo,
                   'content_checksum': checksum,
                   'content': content_display_data['content_data'],
                   'content_raw_url': content_raw_url,
                   'mime_type': mime_type,
                   'language': content_display_data['language'],
                   'breadcrumbs': breadcrumbs,
                   'branches': None,
                   'branch': None})


def content_raw(request, query_string):
    """Django view that produces a raw display of a SWH content identified
    by its hash value.

    The url that points to it is :http:get:`/browse/content/[(algo_hash):](hash)/raw/`

    Args:
        request: input django http request
        query_string: a string of the form "[ALGO_HASH:]HASH" where
            optional ALGO_HASH can be either *sha1*, *sha1_git*, *sha256*,
            or *blake2s256* (default to *sha1*) and HASH the hexadecimal
            representation of the hash value

    Returns:
        The raw bytes of the content.


    """ # noqa

    try:
        algo, checksum = query.parse_hash(query_string)
        checksum = hash_to_hex(checksum)
        content_data, mime_type = request_content(query_string)
    except Exception as exc:
        return handle_view_exception(exc)

    filename = request.GET.get('filename', None)
    if not filename:
        filename = '%s_%s' % (algo, checksum)

    if mime_type.startswith('text/'):
        response = HttpResponse(content_data, content_type="text/plain")
        response['Content-disposition'] = 'filename=%s' % filename
    else:
        response = HttpResponse(content_data,
                                content_type='application/octet-stream')
        response['Content-disposition'] = 'attachment; filename=%s' % filename
    return response
