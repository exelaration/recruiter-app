from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone
from django.utils.html import format_html
from django.core.validators import RegexValidator
from tinymce.models import HTMLField

from django.db import models


class JobPosting(models.Model):
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=100, blank=True, null=True)
    job_link = models.URLField('Job Link', max_length=500)
    enabled = models.BooleanField(default=True)

    def show_job_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.job_link)

    show_job_url.short_description = "Job URL"

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.TextField(blank=False)
    date_time = models.DateField('Event date time', default=timezone.now)
    enabled = models.BooleanField(default=True)
    job_postings = models.ManyToManyField(JobPosting, blank=True,
                                          help_text='Select all Job Postings being recruited for this Event.')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class Candidate(models.Model):
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    email = models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                 message='Phone number must be entered in the format: ''+999999999''. Up to 15 digits allowed.')
    phone = models.CharField(validators=[phone_regex], blank=True,
                             max_length=16, null=True) #validators should be a list

    def __str__(self):
        return "{0} {1} - {2}".format(self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name_plural = 'Candidates'


class Attendance(models.Model):
    candidate = models.ForeignKey(Candidate)
    event = models.ForeignKey(Event)
    selected_job_posting = models.ForeignKey(JobPosting)

    def __str__(self):
        return "{0} attended by {1}".format(self.event, self.candidate)

    class Meta:
        ordering = ['event']
