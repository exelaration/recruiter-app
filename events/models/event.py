from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from events.models.job_posting import JobPosting
from sendemail.models.email_template import EmailTemplate


class Event(models.Model):
    title = models.TextField(blank=False)
    date_time = models.DateField('Event date time', default=timezone.now)
    enabled = models.BooleanField(default=True)
    job_postings = models.ManyToManyField(JobPosting, blank=True,
                                          help_text='Select all Job Postings being recruited for this Event.')
    auto_email = models.BooleanField('Auto send email on registration', default=False)
    auto_email_from = models.EmailField('Auto send from email',
                                        max_length=200, blank=True, null=True)
    email_template = models.ForeignKey(EmailTemplate, blank=True, null=True,
                                       help_text='Select the email template for auto-sending emails at this event.')

    def __str__(self):
        return self.title

    def clean(self):
        if self.auto_email:
            if not self.auto_email_from:
                raise ValidationError({'auto_email_from': ('Auto Email must have corresponding sender defined.')})
            if not self.email_template:
                raise ValidationError({'email_template': ('Auto Email must have corresponding template defined.')})

        return super(Event, self)

    class Meta:
        ordering = ['-date_time']
