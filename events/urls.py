from django.conf.urls import url, include
from rest_framework import routers

from . import views

app_name = 'events'


router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'candidates', views.CandidateViewSet)
router.register(r'attendance', views.AttendanceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]