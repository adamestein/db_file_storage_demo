# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^files/', include('db_file_storage.urls')),
    #
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^console/', include('console.urls')),
    url(r'^game/', include('game.urls')),
)
