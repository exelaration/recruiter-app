from __future__ import unicode_literals
from django.db import models

from events.models.candidate import Candidate
from events.models.event import Event
from events.models.job_posting import JobPosting


class Attendance(models.Model):
    candidate = models.ForeignKey(Candidate)
    event = models.ForeignKey(Event)
    selected_job_posting = models.ForeignKey(JobPosting)

    def __str__(self):
        return "{0} : {1} was attended by {2} : {3}".format(self.event.id, self.event, self.candidate, self.selected_job_posting)

    class Meta:
        ordering = ['event']
