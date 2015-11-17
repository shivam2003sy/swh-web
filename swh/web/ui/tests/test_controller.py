# Copyright (C) 2015  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU Affero General Public License version 3, or any later version
# See top-level LICENSE file for more information

import unittest
import json

from nose.tools import istest
from unittest.mock import patch, MagicMock

from swh.web.ui.tests import test_app


class ApiTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app, _, _ = test_app.init_app()

    @istest
    def info(self):
        # when
        rv = self.app.get('/about')

        self.assertEquals(rv.status_code, 200)
        self.assertIn(b'About', rv.data)

    # @istest
    def search_1(self):
        # when
        rv = self.app.get('/search')

        self.assertEquals(rv.status_code, 200)  # check this api
        self.assertRegexpMatches(rv.data, b'name=q value=>')

    # @istest
    def search_2(self):
        # when
        rv = self.app.get('/search?q=one-hash-to-look-for:another-one')

        self.assertEquals(rv.status_code, 200)  # check this api
        self.assertRegexpMatches(
            rv.data,
            b'name=q value=one-hash-to-look-for:another-one')

    @patch('swh.web.ui.controller.service')
    @istest
    def api_content_with_details(self, mock_service):
        # given
        mock_service.lookup_hash_origin.return_value = {
            'origin_type': 'git',
            'origin_url': 'https://url/user/repo',
            'branch': 'master',
            'revision': '40e71b8614fcd89ccd17ca2b1d9e66c5b00a6d03',
            'path': '/some/path/to/somewhere',
        }

        mock_service.lookup_content.return_value = {
            'data': 'some content data',
            'sha1': '40e71b8614fcd89ccd17ca2b1d9e66c5b00a6d03',
            'sha1_git': 'b4e8f472ffcb01a03875b26e462eb568739f6882',
            'sha256': '83c0e67cc80f60caf1fcbec2d84b0ccd7968b3be4735637006560'
            'cde9b067a4f',
            'length': 17,
            'status': 'visible'
        }

        # when
        rv = self.app.get(
            '/api/1/content/sha1:40e71b8614fcd89ccd17ca2b1d9e66c5b00a6d03/')

        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.mimetype, 'application/json')
        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {
            'origin': {
                'origin_type': 'git',
                'origin_url': 'https://url/user/repo',
                'branch': 'master',
                'revision': '40e71b8614fcd89ccd17ca2b1d9e66c5b00a6d03',
                'path': '/some/path/to/somewhere',
            },
            'data': 'some content data',
            'sha1': '40e71b8614fcd89ccd17ca2b1d9e66c5b00a6d03',
            'sha1_git': 'b4e8f472ffcb01a03875b26e462eb568739f6882',
            'sha256': '83c0e67cc80f60caf1fcbec2d84b0ccd7968b3be4735637006560c'
            'de9b067a4f',
            'length': 17,
            'status': 'visible'
        })

        mock_service.lookup_hash_origin.assert_called_once_with(
            'sha1:40e71b8614fcd89ccd17ca2b1d9e66c5b00a6d03')
        mock_service.lookup_content.assert_called_once_with(
            'sha1:40e71b8614fcd89ccd17ca2b1d9e66c5b00a6d03')

    @patch('swh.web.ui.controller.service')
    @istest
    def api_content_origin_not_found(self, mock_service):
        # given
        mock_service.lookup_hash_origin.return_value = None
        mock_service.lookup_content.return_value = {
            'data': 'some content data..',
            'sha1': '40e71b8614fcd89ccd17ca2b1d9e66c5b00a6d03',
            'sha1_git': 'b4e8f472ffcb01a03875b26e462eb568739f6882',
            'sha256': '83c0e67cc80f60caf1fcbec2d84b0ccd7968b3be4735637006560'
            'cde9b067a4f',
            'length': 19,
            'status': 'absent'
        }

        # when
        rv = self.app.get('/api/1/content/sha1_git:b4e8f472ffcb01a03875b26e4'
                          '62eb568739f6882/')

        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.mimetype, 'application/json')

        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {
            'origin': None,
            'data': 'some content data..',
            'sha1': '40e71b8614fcd89ccd17ca2b1d9e66c5b00a6d03',
            'sha1_git': 'b4e8f472ffcb01a03875b26e462eb568739f6882',
            'sha256': '83c0e67cc80f60caf1fcbec2d84b0ccd7968b3be4735637006560c'
            'de9b067a4f',
            'length': 19,
            'status': 'absent'
        })

        mock_service.lookup_hash_origin.assert_called_once_with(
            'sha1_git:b4e8f472ffcb01a03875b26e462eb568739f6882')
        mock_service.lookup_content.assert_called_once_with(
            'sha1_git:b4e8f472ffcb01a03875b26e462eb568739f6882')

    @patch('swh.web.ui.controller.service')
    @istest
    def api_content_not_found(self, mock_service):
        # given
        mock_service.lookup_content.return_value = None
        mock_service.lookup_hash_origin = MagicMock()

        # when
        rv = self.app.get(
            '/api/1/content/sha256:83c0e67cc80f60caf1fcbec2d84b0ccd7968b3'
            'be4735637006560c/')

        self.assertEquals(rv.status_code, 404)
        self.assertEquals(rv.mimetype, 'application/json')
        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {
            'error': 'Content with sha256:83c0e67cc80f60caf1fcbec2d84b0ccd79'
            '68b3be4735637006560c not found.'
        })

        mock_service.lookup_content.assert_called_once_with(
            'sha256:83c0e67cc80f60caf1fcbec2d84b0ccd7968b3'
            'be4735637006560c')
        mock_service.lookup_hash_origin.called = False

    @patch('swh.web.ui.controller.service')
    @istest
    def api_search(self, mock_service):
        # given
        mock_service.lookup_hash.return_value = True

        # when
        rv = self.app.get('/api/1/search/sha1:blah/')

        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.mimetype, 'application/json')
        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {'found': True})

        mock_service.lookup_hash.assert_called_once_with('sha1:blah')

    @patch('swh.web.ui.controller.service')
    @istest
    def api_search_not_found(self, mock_service):
        # given
        mock_service.lookup_hash.return_value = False

        # when
        rv = self.app.get('/api/1/search/sha1:halb/')

        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.mimetype, 'application/json')
        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {'found': False})

        mock_service.lookup_hash.assert_called_once_with('sha1:halb')

    @patch('swh.web.ui.controller.service')
    @istest
    def api_1_stat_counters_raise_error(self, mock_service):
        # given
        mock_service.stat_counters.side_effect = ValueError(
            'voluntary error to check the bad request middleware.')
        # when
        rv = self.app.get('/api/1/stat/counters')
        # then
        self.assertEquals(rv.status_code, 400)
        self.assertEquals(rv.mimetype, 'application/json')
        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {
            'error': 'voluntary error to check the bad request middleware.'})

    @patch('swh.web.ui.controller.service')
    @istest
    def api_1_stat_counters(self, mock_service):
        # given
        mock_service.stat_counters.return_value = {
            "content": 1770830,
            "directory": 211683,
            "directory_entry_dir": 209167,
            "directory_entry_file": 1807094,
            "directory_entry_rev": 0,
            "entity": 0,
            "entity_history": 0,
            "occurrence": 0,
            "occurrence_history": 19600,
            "origin": 1096,
            "person": 0,
            "release": 8584,
            "revision": 7792,
            "revision_history": 0,
            "skipped_content": 0
        }

        # when
        rv = self.app.get('/api/1/stat/counters')

        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.mimetype, 'application/json')
        self.assertEquals(response_data, {
            "content": 1770830,
            "directory": 211683,
            "directory_entry_dir": 209167,
            "directory_entry_file": 1807094,
            "directory_entry_rev": 0,
            "entity": 0,
            "entity_history": 0,
            "occurrence": 0,
            "occurrence_history": 19600,
            "origin": 1096,
            "person": 0,
            "release": 8584,
            "revision": 7792,
            "revision_history": 0,
            "skipped_content": 0
        })

        mock_service.stat_counters.assert_called_once_with()

    @patch('swh.web.ui.controller.service')
    @patch('swh.web.ui.controller.request')
    @istest
    def api_uploadnsearch(self, mock_request, mock_service):
        # given
        mock_request.files = {'filename': 'simple-filename'}
        mock_service.upload_and_search.return_value = (
            'simple-filename', 'some-hex-sha1', False)

        # when
        rv = self.app.post('/api/1/uploadnsearch/')

        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.mimetype, 'application/json')

        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {'filename': 'simple-filename',
                                          'sha1': 'some-hex-sha1',
                                          'found': False})

        mock_service.upload_and_search.assert_called_once_with(
            'simple-filename')

    @patch('swh.web.ui.controller.service')
    @istest
    def api_origin(self, mock_service):
        # given
        mock_service.lookup_origin.return_value = {
            'id': 'origin-0',
            'lister': 'uuid-lister-0',
            'project': 'uuid-project-0',
            'url': 'ftp://some/url/to/origin/0',
            'type': 'ftp'}

        # when
        rv = self.app.get('/api/1/origin/origin-0')

        # then
        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.mimetype, 'application/json')

        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {
            'origin': {
                'id': 'origin-0',
                'lister': 'uuid-lister-0',
                'project': 'uuid-project-0',
                'url': 'ftp://some/url/to/origin/0',
                'type': 'ftp'
            }
        })

    @patch('swh.web.ui.controller.service')
    @istest
    def api_origin_not_found(self, mock_service):
        # given
        mock_service.lookup_origin.return_value = None

        # when
        rv = self.app.get('/api/1/origin/origin-0')

        # then
        self.assertEquals(rv.status_code, 404)
        self.assertEquals(rv.mimetype, 'application/json')
        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {
            'error': 'Origin with id origin-0 not found.'
        })

    @patch('swh.web.ui.controller.service')
    @istest
    def api_release(self, mock_service):
        # given
        mock_service.lookup_release.return_value = {
            'id': 'release-0',
            'revision': 'revision-sha1',
            'author': 'author-id',
        }

        # when
        rv = self.app.get('/api/1/release/release-0')

        # then
        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.mimetype, 'application/json')

        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {
            'release': {
                'id': 'release-0',
                'revision': 'revision-sha1',
                'author': 'author-id',
            }
        })

    @patch('swh.web.ui.controller.service')
    @istest
    def api_release_not_found(self, mock_service):
        # given
        mock_service.lookup_release.return_value = None

        # when
        rv = self.app.get('/api/1/release/release-0')

        # then
        self.assertEquals(rv.status_code, 404)
        self.assertEquals(rv.mimetype, 'application/json')

        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {
            'error': 'Release with sha1_git release-0 not found.'
        })

    @patch('swh.web.ui.controller.service')
    @istest
    def api_revision(self, mock_service):
        # given
        mock_revision = {
            'id': '18d8be353ed3480476f032475e7c233eff7371d5',
            'directory': '7834ef7e7c357ce2af928115c6c6a42b7e2a44e6',
            'author_name': 'Software Heritage',
            'author_email': 'robot@softwareheritage.org',
            'committer_name': 'Software Heritage',
            'committer_email': 'robot@softwareheritage.org',
            'message': 'synthetic revision message',
            'date_offset': 0,
            'committer_date_offset': 0,
            'parents': [],
            'type': 'tar',
            'synthetic': True,
            'metadata': {
                'original_artifact': [{
                    'archive_type': 'tar',
                    'name': 'webbase-5.7.0.tar.gz',
                    'sha1': '147f73f369733d088b7a6fa9c4e0273dcd3c7ccd',
                    'sha1_git': '6a15ea8b881069adedf11feceec35588f2cfe8f1',
                    'sha256': '401d0df797110bea805d358b85bcc1ced29549d3d73f'
                    '309d36484e7edf7bb912'
                }]
            },
        }
        mock_service.lookup_revision.return_value = mock_revision

        # when
        rv = self.app.get('/api/1/revision/revision-0')

        # then
        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.mimetype, 'application/json')

        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {"revision": mock_revision})

    @patch('swh.web.ui.controller.service')
    @istest
    def api_revision_not_found(self, mock_service):
        # given
        mock_service.lookup_revision.return_value = None

        # when
        rv = self.app.get('/api/1/revision/revision-0')

        # then
        self.assertEquals(rv.status_code, 404)
        self.assertEquals(rv.mimetype, 'application/json')

        response_data = json.loads(rv.data.decode('utf-8'))
        self.assertEquals(response_data, {
            'error': 'Revision with sha1_git revision-0 not found.'})
