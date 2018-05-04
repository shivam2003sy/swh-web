# Copyright (C) 2017-2018  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU Affero General Public License version 3, or any later version
# See top-level LICENSE file for more information

from django.conf.urls import url
from django.shortcuts import render

import swh.web.browse.views.directory # noqa
import swh.web.browse.views.content # noqa
import swh.web.browse.views.identifiers # noqa
import swh.web.browse.views.origin # noqa
import swh.web.browse.views.person # noqa
import swh.web.browse.views.release # noqa
import swh.web.browse.views.revision # noqa
import swh.web.browse.views.snapshot # noqa

from swh.web.browse.browseurls import BrowseUrls


def _default_browse_view(request):
    return render(request, 'browse.html',
                  {'heading': 'Browse',
                   'empty_browse': True})


def _browse_help_view(request):
    return render(request, 'browse-help.html',
                  {'heading': 'Help'})


def _browse_search_view(request):
    return render(request, 'browse-search.html',
                  {'heading': 'Search'})


def _browse_vault_view(request):
    return render(request, 'browse-vault-ui.html',
                  {'heading': 'Vault'})


urlpatterns = [
    url(r'^$', _default_browse_view, name='browse-mainpage'),
    url(r'^help/$', _browse_help_view, name='browse-help'),
    url(r'^search/$', _browse_search_view, name='browse-search'),
    url(r'^vault/$', _browse_vault_view, name='browse-vault')
]

urlpatterns += BrowseUrls.get_url_patterns()
