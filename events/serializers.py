from rest_framework import serializers

from .models import Event, Candidate, JobPosting, Attendance

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'enabled', 'title')

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'first_name', 'last_name', 'email', 'phone')

class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id', 'event_id', 'candidate_id', 'selected_job_posting_id')