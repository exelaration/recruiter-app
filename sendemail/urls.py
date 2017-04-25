from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'events'

urlpatterns = [
    url(r'^(?P<event_id>[0-9]+)/sendtest/(?P<attendance_id>[0-9]+)/$', views.send_test_email, name='send_test_email'),
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]

