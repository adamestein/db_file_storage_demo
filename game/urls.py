# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.conf.urls import patterns, url
from django.views.generic import ListView, CreateView, UpdateView
from game.forms import FormGame
from game.models import Game


urlpatterns = patterns('game.views',
    url(
        r'^list/$',
        ListView.as_view(
            queryset = Game.objects.all(),
            template_name = 'generic_list.html'
        ),
        name = 'game.list'
    ),
    url(
        r'^add/$',
        CreateView.as_view(
            model = Game,
            form_class = FormGame,
            template_name = 'generic_form.html',
            success_url = reverse_lazy('game.list')
        ),
        name = 'game.add'
    ),
    url(
        r'^edit/(?P<pk>\d+)/$',
        UpdateView.as_view(
            model = Game,
            form_class = FormGame,
            template_name = 'generic_form.html',
            success_url = reverse_lazy('game.list')
        ),
        name = 'game.edit'
    ),
)
