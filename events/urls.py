from django.conf.urls import url

from . import views

app_name = 'events'

urlpatterns = [
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<event_id>[0-9]+)?/?$', views.edit, name='edit'),
    url(r'^$', views.index, name='index'),
]
