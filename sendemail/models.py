from __future__ import unicode_literals
from django.db import models
from tinymce.models import HTMLField
from events.models import Event, Candidate


class EmailTemplate(models.Model):
    subject = models.CharField('Subject', max_length=100)
    body = HTMLField()
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return "{0} - {1}".format(self.id, self.subject)

    class Meta:
        ordering = ['id', 'subject']


class EmailLog(models.Model):
    event_id = models.ForeignKey(Event)
    candidate_id = models.ForeignKey(Candidate)
    to_address = models.CharField('To', max_length=200, editable=False)
    from_address = models.CharField('From', max_length=200, editable=False)
    subject = models.CharField('Subject', max_length=100, editable=False)
    time_sent = models.DateTimeField(editable=False)
    body = HTMLField(editable=False)
    response = models.TextField(editable=False)
