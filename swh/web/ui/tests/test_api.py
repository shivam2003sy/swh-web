# Copyright (C) 2015  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

import unittest

from nose.tools import istest

from swh.web.ui import api


class ApiTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    @istest
    def info(self):
        # when
        rv = self.app.get('/info')

        self.assertEquals(rv.status_code, 200)
        self.assertEquals(rv.data, b'Dev SWH UI')

    @istest
    def main_redirects_to_info(self):
        # when
        rv = self.app.get('/', follow_redirects=False)

        self.assertEquals(rv.status_code, 302)  # check that it redirects to /info

    @istest
    def public_redirects_to_search(self):
        # when
        rv = self.app.get('/public', follow_redirects=False)

        self.assertEquals(rv.status_code, 302)  # check that it redirects to /public/search

    @istest
    def search_1(self):
        # when
        rv = self.app.get('/public/search')

        self.assertEquals(rv.status_code, 200)  # check this api
        self.assertRegexpMatches(rv.data, b'name=nb_hashes value=2')
        self.assertRegexpMatches(rv.data, b'name=hash1 value=>')
        self.assertRegexpMatches(rv.data, b'name=hash2 value=>')

    @istest
    def search_2(self):
        # when
        rv = self.app.get('/public/search?nb_hashes=2&hash1=something-to-look-for&hash2=another-thingy')

        self.assertEquals(rv.status_code, 200)  # check this api
        self.assertRegexpMatches(rv.data, b'name=nb_hashes value=2')
        self.assertRegexpMatches(rv.data, b'name=hash1 value=something-to-look-for>')
        self.assertRegexpMatches(rv.data, b'name=hash2 value=another-thingy>')
