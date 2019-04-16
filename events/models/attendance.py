from __future__ import unicode_literals
from django.db import models

from events.models.candidate import Candidate
from events.models.event import Event
from events.models.job_posting import JobPosting
from django.db import connection

class Attendance(models.Model):
    candidate = models.ForeignKey(Candidate)
    event = models.ForeignKey(Event)
    selected_job_posting = models.ForeignKey(JobPosting)

    def __str__(self):
        return "{0} : {1} was attended by {2} : {3}".format(self.event.id, self.event, self.candidate, self.selected_job_posting)

    def candidates_for_event(event):
        sql = """
            SELECT can.first_name as first_name, can.last_name, can.phone, can.email, string_agg(jp.title, ', ')
            FROM public.events_attendance att
            JOIN public.events_candidate can on can.id = att.candidate_id
            JOIN public.events_event evt on evt.id = att.event_id
            JOIN public.events_jobposting jp on jp.id = att.selected_job_posting_id
            WHERE evt.id = """ + event + """
            GROUP BY can.id
            """
        cursor = connection.cursor()
        cursor.execute(sql)
        return [ EventCandidate(val) for val in cursor.fetchall()]

    class Meta:
        ordering = ['event']

class EventCandidate:
    def __init__(self, list):
        self.first_name = list[0]
        self.last_name = list[1]
        self.phone = list[2]
        self.email = list[3]
        self.postings = list[4]
        self.email_error = False
        
