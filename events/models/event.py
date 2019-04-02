from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

from events.models.job_posting import JobPosting
from sendemail.models.email_template import EmailTemplate


class Event(models.Model):
    title = models.TextField(blank=False)
    date_time = models.DateField('Event date time', default=timezone.now)
    enabled = models.BooleanField(default=True)
    job_postings = models.ManyToManyField(JobPosting, blank=True,
                                          help_text='Select all Job Postings being recruited for this Event.')
    auto_email = models.BooleanField(default=False, verbose_name='Auto send Email on Registration')
    email_template = models.ForeignKey(EmailTemplate, blank=True,
                                       help_text='Select the email template for auto-sending emails at this event.')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
