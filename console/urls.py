# -*- coding: utf-8 -*-

from console.forms import FormConsole
from console.models import Console
from django.core.urlresolvers import reverse_lazy
from django.conf.urls import patterns, url
from django.views.generic import ListView, CreateView, UpdateView


urlpatterns = patterns('',
    url(
        r'^list/$',
        ListView.as_view(
            queryset = Console.objects.all(),
            template_name = 'generic_list.html'
        ),
        name='console.list'
    ),
    url(
        r'^add/$',
        CreateView.as_view(
            model = Console,
            form_class = FormConsole,
            template_name = 'generic_form.html',
            success_url = reverse_lazy('console.list')
        ),
        name='console.add'
    ),
    url(
        r'^edit/(?P<pk>\d+)/$',
        UpdateView.as_view(
            model = Console,
            form_class = FormConsole,
            template_name = 'generic_form.html',
            success_url = reverse_lazy('console.list')
        ),
        name='console.edit'
    ),
)
