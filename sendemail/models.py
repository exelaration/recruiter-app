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
    to_address = models.CharField('To', max_length=200)
    cc_address = models.CharField('CC', max_length=200, blank=True, null=True)
    bcc_address = models.CharField('BCC', max_length=200, blank=True, null=True)
    from_address = models.CharField('From', max_length=200)
    subject = models.CharField('Subject', max_length=100)
    time_sent = models.DateTimeField(auto_now=True)
    body = HTMLField()
    response = models.TextField(editable=False, blank=True, null=True)
