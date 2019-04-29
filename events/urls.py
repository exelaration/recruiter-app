from django.conf.urls import url

from . import views
from . import email_template_views
from . import job_posting_views

app_name = 'events'

urlpatterns = [
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<event_id>[0-9]+)?/?$', views.edit, name='edit'),
    url(r'^templates/edit/(?P<template_id>[0-9]+)?/?$', email_template_views.edit, name='edit_email_template'),
    url(r'^templates$', email_template_views.index, name='email_template_index'),
    url(r'^postings/edit/(?P<job_posting_id>[0-9]+)?/?$', job_posting_views.edit, name='job_posting_template'),
    url(r'^postings$', job_posting_views.index, name='job_posting_template'),
    url(r'^$', views.index, name='index'),
]
