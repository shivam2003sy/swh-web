# Copyright (C) 2015  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU Affero General Public License version 3, or any later version
# See top-level LICENSE file for more information

from types import GeneratorType

from flask import request, url_for, Response, redirect

from swh.web.ui import service, utils
from swh.web.ui.exc import BadInputExc, NotFoundExc
from swh.web.ui.main import app


@app.route('/api/1/stat/counters/')
def api_stats():
    """Return statistics on SWH storage.

    Returns:
        SWH storage's statistics.

    """
    return service.stat_counters()


@app.route('/api/1/search/')
@app.route('/api/1/search/<string:q>/')
def api_search(q='sha1:bd819b5b28fcde3bf114d16a44ac46250da94ee5'):
    """Search a content per hash.

    Args:
        q is of the form algo_hash:hash with algo_hash in
        (sha1, sha1_git, sha256).

    Returns:
        Dictionary with 'found' key and the associated result.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.

    Example:
        GET /api/1/search/sha1:bd819b5b28fcde3bf114d16a44ac46250da94ee5/

    """
    r = service.lookup_hash(q).get('found')
    return {'found': True if r else False}


def _api_lookup(criteria,
                lookup_fn,
                error_msg_if_not_found,
                enrich_fn=lambda x: x,
                *args):
    """Capture a redundant behavior of:
    - looking up the backend with a criteria (be it an identifier or checksum)
    passed to the function lookup_fn
    - if nothing is found, raise an NotFoundExc exception with error
    message error_msg_if_not_found.
    - Otherwise if something is returned:
        - either as list, map or generator, map the enrich_fn function to it
        and return the resulting data structure as list.
        - either as dict and pass to enrich_fn and return the dict enriched.

    Args:
        - criteria: discriminating criteria to lookup
        - lookup_fn: function expects one criteria and optional supplementary
        *args.
        - error_msg_if_not_found: if nothing matching the criteria is found,
        raise NotFoundExc with this error message.
        - enrich_fn: Function to use to enrich the result returned by
        lookup_fn. Default to the identity function if not provided.
        - *args: supplementary arguments to pass to lookup_fn.

    Raises:
        NotFoundExp or whatever `lookup_fn` raises.

    """
    res = lookup_fn(criteria, *args)
    if not res:
        raise NotFoundExc(error_msg_if_not_found)
    if isinstance(res, (map, list, GeneratorType)):
        enriched_data = []
        for e in res:
            enriched_data.append(enrich_fn(e))
        return enriched_data
    return enrich_fn(res)


@app.route('/api/1/origin/')
@app.route('/api/1/origin/<int:origin_id>/')
def api_origin(origin_id=1):
    """Return information about origin with id origin_id.


    Args:
        origin_id: the origin's identifier.

    Returns:
        Information on the origin if found.

    Raises:
        NotFoundExc if the origin is not found.

    Example:
        GET /api/1/origin/1/

    """
    return _api_lookup(
        origin_id, lookup_fn=service.lookup_origin,
        error_msg_if_not_found='Origin with id %s not found.' % origin_id)


@app.route('/api/1/person/')
@app.route('/api/1/person/<int:person_id>/')
def api_person(person_id=1):
    """Return information about person with identifier person_id.

    Args:
        person_id: the person's identifier.

    Returns:
        Information on the person if found.

    Raises:
        NotFoundExc if the person is not found.

    Example:
        GET /api/1/person/1/

    """
    return _api_lookup(
        person_id, lookup_fn=service.lookup_person,
        error_msg_if_not_found='Person with id %s not found.' % person_id)


@app.route('/api/1/release/')
@app.route('/api/1/release/<string:sha1_git>/')
def api_release(sha1_git='1e951912027ea6873da6985b91e50c47f645ae1a'):
    """Return information about release with id sha1_git.

    Args:
        sha1_git: the release's hash.

    Returns:
        Information on the release if found.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if the release is not found.

    Example:
        GET /api/1/release/b307094f00c3641b0c9da808d894f3a325371414

    """
    error_msg = 'Release with sha1_git %s not found.' % sha1_git
    return _api_lookup(
        sha1_git,
        lookup_fn=service.lookup_release,
        error_msg_if_not_found=error_msg,
        enrich_fn=utils.enrich_release)


def _revision_directory_by(revision, path, request_path,
                           limit=100, with_data=False):
    """Compute the revision matching criterion's directory or content data.

    Args:
        revision: dictionary of criterions representing a revision to lookup
        path: directory's path to lookup
        request_path: request path which holds the original context to
        limit: optional query parameter to limit the revisions log
        (default to 100). For now, note that this limit could impede the
        transitivity conclusion about sha1_git not being an ancestor of
        with_data: indicate to retrieve the content's raw data if path resolves
        to a content.

    """
    def enrich_directory_local(dir, context_url=request_path):
        return utils.enrich_directory(dir, context_url)

    rev_id, result = service.lookup_directory_through_revision(
        revision, path, limit=limit, with_data=with_data)

    content = result['content']
    if result['type'] == 'dir':  # dir_entries
        result['content'] = list(map(enrich_directory_local, content))
    else:  # content
        result['content'] = utils.enrich_content(content)

    return result


@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/directory/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/directory/<path:path>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/directory/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/directory/<path:path>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/ts/<string:ts>'
           '/directory/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/ts/<string:ts>'
           '/directory/<path:path>/')
def api_directory_through_revision_origin(origin_id=1,
                                          branch_name="refs/heads/master",
                                          ts=None,
                                          path=None,
                                          with_data=False):
    """Display directory or content information through a revision identified
    by origin/branch/timestamp.

    Args:
        origin_id: origin's identifier (default to 1).
        branch_name: the optional branch for the given origin (default
        to master).
        timestamp: optional timestamp (default to the nearest time
        crawl of timestamp).
        path: Path to directory or file to display.
        with_data: indicate to retrieve the content's raw data if path resolves
        to a content.

    Returns:
        Information on the directory or content pointed to by such revision.

    Raises:
        NotFoundExc if the revision is not found or the path pointed to
        is not found.

    """
    if ts:
        ts = utils.parse_timestamp(ts)

    return _revision_directory_by(
        {
            'origin_id': origin_id,
            'branch_name': branch_name,
            'ts': ts
        },
        path,
        request.path,
        with_data=with_data)


@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/history/<sha1_git>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/history/<sha1_git>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/ts/<string:ts>'
           '/history/<sha1_git>/')
def api_revision_history_through_origin(origin_id=1,
                                        branch_name="refs/heads/master",
                                        ts=None,
                                        sha1_git=None):
    """
    Return information about revision sha1_git, limited to the
    sub-graph of all transitive parents of the revision root identified
    by (origin_id, branch_name, ts).
    Given sha1_git_root such root revision's identifier, in other words,
    sha1_git is an ancestor of sha1_git_root.

    Args:
        origin_id: origin's identifier (default to 1).
        branch_name: the optional branch for the given origin (default
        to master).
        timestamp: optional timestamp (default to the nearest time
        crawl of timestamp).
        sha1_git: one of sha1_git_root's ancestors.
        limit: optional query parameter to limit the revisions log
        (default to 100). For now, note that this limit could impede the
        transitivity conclusion about sha1_git not being an ancestor of
        sha1_git_root (even if it is).

    Returns:
        Information on sha1_git if it is an ancestor of sha1_git_root
        including children leading to sha1_git_root.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if either revision is not found or if sha1_git is not an
        ancestor of sha1_git_root.

    """
    limit = int(request.args.get('limit', '100'))

    if ts:
        ts = utils.parse_timestamp(ts)

    rev_root, revision = service.lookup_revision_with_context_by(
        origin_id, branch_name, ts, sha1_git, limit)

    if not revision:
        raise NotFoundExc(
            "Possibly sha1_git '%s' is not an ancestor of sha1_git_root '%s' "
            "sha1_git_root being the revision's identifier pointed to by "
            "(origin_id: %s, branch_name: %s, ts: %s)." % (sha1_git,
                                                           rev_root['id'],
                                                           origin_id,
                                                           branch_name,
                                                           ts))

    return utils.enrich_revision(revision, context=rev_root['id'])


@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/history/<sha1_git>'
           '/directory/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/history/<sha1_git>'
           '/directory/<path:path>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/history/<sha1_git>'
           '/directory/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/history/<sha1_git>'
           '/directory/<path:path>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/ts/<string:ts>'
           '/history/<sha1_git>'
           '/directory/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/ts/<string:ts>'
           '/history/<sha1_git>'
           '/directory/<path:path>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/ts/<string:ts>'
           '/history/<sha1_git>'
           '/directory/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/ts/<string:ts>'
           '/history/<sha1_git>'
           '/directory/<path:path>/')
def api_directory_through_revision_with_origin_history(
        origin_id=1,
        branch_name="refs/heads/master",
        ts=None,
        sha1_git=None,
        path=None,
        with_data=False):
    """Return information about directory or content pointed to by the
    revision defined as: revision sha1_git, limited to the sub-graph
    of all transitive parents of sha1_git_root (being the identified
    sha1 by looking up origin_id/branch_name/ts)

    Args:
        origin_id: origin's identifier (default to 1).
        branch_name: the optional branch for the given origin (default
        to master).
        timestamp: optional timestamp (default to the nearest time
        crawl of timestamp).
        sha1_git: one of sha1_git_root's ancestors.
        path: optional directory or content pointed to by that revision.
        limit: optional query parameter to limit the revisions log
        (default to 100). For now, note that this limit could impede the
        transitivity conclusion about sha1_git not being an ancestor of
        sha1_git_root (even if it is).
        with_data: indicate to retrieve the content's raw data if path resolves
        to a content.

    Returns:
        Information on the directory pointed to by that revision.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if either revision is not found or if sha1_git is not an
        ancestor of sha1_git_root or the path referenced does not exist.

    """
    limit = int(request.args.get('limit', '100'))

    if ts:
        ts = utils.parse_timestamp(ts)

    return _revision_directory_by(
        {
            'origin_id': origin_id,
            'branch_name': branch_name,
            'ts': ts,
            'sha1_git': sha1_git
        },
        path,
        request.path,
        limit=limit, with_data=with_data)


@app.route('/api/1/revision'
           '/origin/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/branch/<path:branch_name>'
           '/ts/<string:ts>/')
@app.route('/api/1/revision'
           '/origin/<int:origin_id>'
           '/ts/<string:ts>/')
def api_revision_with_origin(origin_id=1,
                             branch_name="refs/heads/master",
                             ts=None):
    """Instead of having to specify a (root) revision by SHA1_GIT, users
    might want to specify a place and a time. In SWH a "place" is an
    origin; a "time" is a timestamp at which some place has been
    observed by SWH crawlers.

    Args:
        origin_id: origin's identifier (default to 1).
        branch_name: the optional branch for the given origin (default
        to master).
        timestamp: optional timestamp (default to the nearest time
        crawl of timestamp).

    Returns:
        Information on the revision if found.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if the revision is not found.

    """
    if ts:
        ts = utils.parse_timestamp(ts)

    return _api_lookup(
        origin_id,
        service.lookup_revision_by,
        'Revision with (origin_id: %s, branch_name: %s'
        ', ts: %s) not found.' % (origin_id,
                                  branch_name,
                                  ts),
        utils.enrich_revision,
        branch_name,
        ts)


@app.route('/api/1/revision/')
@app.route('/api/1/revision/<string:sha1_git>/')
def api_revision(sha1_git='a585d2b738bfa26326b3f1f40f0f1eda0c067ccf'):
    """Return information about revision with id sha1_git.

    Args:
        sha1_git: the revision's hash.

    Returns:
        Information on the revision if found.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if the revision is not found.

    Example:
        GET /api/1/revision/baf18f9fc50a0b6fef50460a76c33b2ddc57486e

    """
    return _api_lookup(
        sha1_git,
        lookup_fn=service.lookup_revision,
        error_msg_if_not_found='Revision with sha1_git %s not'
                               ' found.' % sha1_git,
        enrich_fn=utils.enrich_revision)


@app.route('/api/1/revision/<string:sha1_git>/directory/')
@app.route('/api/1/revision/<string:sha1_git>/directory/<path:dir_path>/')
def api_revision_directory(sha1_git='a585d2b738bfa26326b3f1f40f0f1eda0c067ccf',
                           dir_path=None,
                           with_data=False):
    """Return information on directory pointed by revision with sha1_git.
    If dir_path is not provided, display top level directory.
    Otherwise, display the directory pointed by dir_path (if it exists).

    Args:
        sha1_git: revision's hash.
        dir_path: optional directory pointed to by that revision.
        with_data: indicate to retrieve the content's raw data if path resolves
        to a content

    Returns:
        Information on the directory pointed to by that revision.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc either if the revision is not found or the path referenced
        does not exist

    Example:
        GET /api/1/revision/baf18f9fc50a0b6fef50460a76c33b2ddc57486e/directory/

    """
    return _revision_directory_by(
        {
            'sha1_git': sha1_git
        },
        dir_path,
        request.path,
        with_data=with_data)


@app.route('/api/1/revision/<string:sha1_git_root>/history/<sha1_git>/')
def api_revision_history(sha1_git_root, sha1_git):
    """Return information about revision sha1_git, limited to the
    sub-graph of all transitive parents of sha1_git_root.

    In other words, sha1_git is an ancestor of sha1_git_root.

    Args:
        sha1_git_root: latest revision of the browsed history.
        sha1_git: one of sha1_git_root's ancestors.
        limit: optional query parameter to limit the revisions log
        (default to 100). For now, note that this limit could impede the
        transitivity conclusion about sha1_git not being an ancestor of
        sha1_git_root (even if it is).

    Returns:
        Information on sha1_git if it is an ancestor of sha1_git_root
        including children leading to sha1_git_root.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if either revision is not found or if sha1_git is not an
        ancestor of sha1_git_root.

    """
    limit = int(request.args.get('limit', '100'))

    if sha1_git == sha1_git_root:
        return redirect(url_for('api_revision',
                                sha1_git=sha1_git,
                                limit=limit))

    revision = service.lookup_revision_with_context(sha1_git_root,
                                                    sha1_git,
                                                    limit)
    if not revision:
        raise NotFoundExc(
            "Possibly sha1_git '%s' is not an ancestor of sha1_git_root '%s'"
            % (sha1_git, sha1_git_root))

    return utils.enrich_revision(revision, context=sha1_git_root)


@app.route('/api/1/revision/<string:sha1_git_root>'
           '/history/<sha1_git>'
           '/directory/')
@app.route('/api/1/revision/<string:sha1_git_root>'
           '/history/<sha1_git>'
           '/directory/<path:dir_path>/')
def api_revision_history_directory(sha1_git_root, sha1_git,
                                   dir_path=None, with_data=False):
    """Return information about directory pointed to by the revision
    defined as: revision sha1_git, limited to the sub-graph of all
    transitive parents of sha1_git_root.

    Args:
        sha1_git_root: latest revision of the browsed history.
        sha1_git: one of sha1_git_root's ancestors.
        dir_path: optional directory pointed to by that revision.
        limit: optional query parameter to limit the revisions log
        (default to 100). For now, note that this limit could impede the
        transitivity conclusion about sha1_git not being an ancestor of
        sha1_git_root (even if it is).
        with_data: indicate to retrieve the content's raw data if path resolves
        to a content.

    Returns:
        Information on the directory pointed to by that revision.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if either revision is not found or if sha1_git is not an
        ancestor of sha1_git_root or the path referenced does not exist

    """
    limit = int(request.args.get('limit', '100'))

    if sha1_git == sha1_git_root:
        return redirect(url_for('api_revision_directory',
                                sha1_git=sha1_git,
                                dir_path=dir_path),
                        code=301)

    return _revision_directory_by(
        {
            'sha1_git_root': sha1_git_root,
            'sha1_git': sha1_git
        },
        dir_path,
        request.path,
        limit=limit, with_data=with_data)


@app.route('/api/1/revision/<string:sha1_git>/log/')
def api_revision_log(sha1_git):
    """Show all revisions (~git log) starting from sha1_git.
       The first element returned is the given sha1_git.

    Args:
        sha1_git: the revision's hash.
        limit: optional query parameter to limit the revisions log
        (default to 100).

    Returns:
        Information on the revision if found.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if the revision is not found.

    """
    limit = int(request.args.get('limit', '100'))

    def lookup_revision_log_with_limit(s, limit=limit):
        return service.lookup_revision_log(s, limit)

    error_msg = 'Revision with sha1_git %s not found.' % sha1_git
    return _api_lookup(sha1_git,
                       lookup_fn=lookup_revision_log_with_limit,
                       error_msg_if_not_found=error_msg,
                       enrich_fn=utils.enrich_revision)


@app.route('/api/1/directory/')
@app.route('/api/1/directory/<string:sha1_git>/')
@app.route('/api/1/directory/<string:sha1_git>/<path:path>/')
def api_directory(sha1_git='dcf3289b576b1c8697f2a2d46909d36104208ba3',
                  path=None):
    """Return information about release with id sha1_git.

    Args:
        sha1_git: Directory's sha1_git.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if the content is not found.

    Example:
        GET /api/1/directory/8d7dc91d18546a91564606c3e3695a5ab568d179

    """
    if path:
        error_msg_path = ('Entry with path %s relative to directory '
                          'with sha1_git %s not found.') % (path, sha1_git)
        return _api_lookup(
            sha1_git,
            service.lookup_directory_with_path,
            error_msg_path,
            utils.enrich_directory,
            path)
    else:
        error_msg_nopath = 'Directory with sha1_git %s not found.' % sha1_git
        return _api_lookup(
            sha1_git,
            service.lookup_directory,
            error_msg_nopath,
            utils.enrich_directory)


# @app.route('/api/1/browse/')
# @app.route('/api/1/browse/<string:q>/')
def api_content_checksum_to_origin(q='sha1_git:26ac0281bc74e9bd8a4a4aab1c7c7a'
                                   '0c19d4436c'):
    """Return content information up to one of its origin if the content
    is found.

    Args:
        q is of the form algo_hash:hash with algo_hash in
        (sha1, sha1_git, sha256).

    Returns:
        Information on one possible origin for such content.

    Raises:
        BadInputExc in case of unknown algo_hash or bad hash.
        NotFoundExc if the content is not found.

    Example:
        GET /api/1/browse/sha1_git:88b9b366facda0b5ff8d8640ee9279bed346f242

    """
    found = service.lookup_hash(q)['found']
    if not found:
        raise NotFoundExc('Content with %s not found.' % q)

    return service.lookup_hash_origin(q)


@app.route('/api/1/content/<string:q>/raw/')
def api_content_raw(q):
    """Return content's raw data if content is found.

    Args:
        q is of the form (algo_hash:)hash with algo_hash in
        (sha1, sha1_git, sha256).
        When algo_hash is not provided, 'hash' is considered sha1.

    Returns:
        Content's raw data in application/octet-stream.

    Raises:
        - BadInputExc in case of unknown algo_hash or bad hash
        - NotFoundExc if the content is not found.

    """
    def generate(content):
        yield content['data']

    content = service.lookup_content_raw(q)
    if not content:
        raise NotFoundExc('Content with %s not found.' % q)

    return Response(generate(content), mimetype='application/octet-stream')


@app.route('/api/1/content/')
@app.route('/api/1/content/<string:q>/')
def api_content_metadata(q='sha256:e2c76e40866bb6b28916387bdfc8649beceb'
                         '523015738ec6d4d540c7fe65232b'):
    """Return content information if content is found.

    Args:
        q is of the form (algo_hash:)hash with algo_hash in
        (sha1, sha1_git, sha256).
        When algo_hash is not provided, 'hash' is considered sha1.

    Returns:
        Content's information.

    Raises:
        - BadInputExc in case of unknown algo_hash or bad hash.
        - NotFoundExc if the content is not found.

    Example:
        GET /api/1/content/sha256:e2c76e40866bb6b28916387bdfc8649beceb
                                  523015738ec6d4d540c7fe65232b

    """
    return _api_lookup(
        q,
        lookup_fn=service.lookup_content,
        error_msg_if_not_found='Content with %s not found.' % q,
        enrich_fn=utils.enrich_content)


@app.route('/api/1/entity/')
@app.route('/api/1/entity/<string:uuid>/')
def api_entity_by_uuid(uuid='5f4d4c51-498a-4e28-88b3-b3e4e8396cba'):
    """Return content information if content is found.

    Args:
        q is of the form (algo_hash:)hash with algo_hash in
        (sha1, sha1_git, sha256).
        When algo_hash is not provided, 'hash' is considered sha1.

    Returns:
        Content's information.

    Raises:
        - BadInputExc in case of unknown algo_hash or bad hash.
        - NotFoundExc if the content is not found.

    Example:
        - GET /api/1/entity/5f4d4c51-498a-4e28-88b3-b3e4e8396cba/
        - GET /api/1/entity/7c33636b-8f11-4bda-89d9-ba8b76a42cec/

    """
    return _api_lookup(
        uuid,
        lookup_fn=service.lookup_entity_by_uuid,
        error_msg_if_not_found="Entity with uuid '%s' not found." % uuid,
        enrich_fn=utils.enrich_entity)


@app.route('/api/1/uploadnsearch/', methods=['POST'])
def api_uploadnsearch():
    """Upload the file's content in the post body request.
       Compute its hash and determine if it exists in the storage.

    Args:
        request.files filled with the filename's data to upload.

    Returns:
        Dictionary with 'sha1', 'filename' and 'found' predicate depending
        on whether we find it or not.

    Raises:
        BadInputExc in case of the form submitted is incorrect.

    """
    file = request.files.get('filename')
    if not file:
        raise BadInputExc("Bad request, missing 'filename' entry in form.")

    return service.upload_and_search(file)
