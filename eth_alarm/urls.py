# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(
        r'^$', TemplateView.as_view(template_name='home.html'),
        name="site-index",
    ),
    url(
        r'^source/$', TemplateView.as_view(template_name='source.html'),
        name="source-code",
    ),
    url(
        r'^bug-bounty/$', TemplateView.as_view(template_name='bug_bounty.html'),
        name="bug-bounty",
    ),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
