# Copyright (C) 2017-2018  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU Affero General Public License version 3, or any later version
# See top-level LICENSE file for more information

from django.conf import settings
from django.conf.urls import (
    url, include, handler400, handler403, handler404, handler500
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.views import serve
from django.shortcuts import render
from django.views.generic.base import RedirectView

from django_js_reverse.views import urls_js

from swh.web.common.exc import (
    swh_handle400, swh_handle403, swh_handle404, swh_handle500
)

favicon_view = RedirectView.as_view(url='/static/img/icons/swh-logo-32x32.png',
                                    permanent=True)


def default_view(request):
    return render(request, "homepage.html")


urlpatterns = [
    url(r'^favicon\.ico$', favicon_view),
    url(r'^api/', include('swh.web.api.urls')),
    url(r'^browse/', include('swh.web.browse.urls')),
    url(r'^$', default_view, name='swh-web-homepage'),
    url(r'^jsreverse/$', urls_js, name='js_reverse')
]

# enable to serve compressed assets through django development server
if settings.DEBUG:
    static_pattern = r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:]
    urlpatterns.append(url(static_pattern, serve))
else:
    urlpatterns += staticfiles_urlpatterns()

handler400 = swh_handle400 # noqa
handler403 = swh_handle403 # noqa
handler404 = swh_handle404 # noqa
handler500 = swh_handle500 # noqa
