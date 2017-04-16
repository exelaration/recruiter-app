from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone
from django.utils.html import format_html

from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=70)
    date_time = models.DateField('Event date time', default=timezone.now)
    description = models.TextField(blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_time']


class JobPosting(models.Model):
    title = models.CharField(max_length=300)
    job_link = models.URLField('Job Link', max_length=500)

    def show_job_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.job_link)

    show_job_url.short_description = "Job URL"

    def __str__(self):
        return self.title


class Candidate(models.Model):
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    phone = models.CharField(max_length=20, default=None, blank=True, null=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return "{0} {1} - {2}".format(self.first_name, self.last_name, self.email)

    class Meta:
        verbose_name_plural = 'Candidate'


class Application(models.Model):
    candidate = models.ForeignKey(Candidate)
    event = models.ForeignKey(Event)

    def __str__(self):
        return "Event: {0}, {1}, {2}, {3}, {4}".format(self.event.name, self.candidate.first_name,
                                                       self.candidate.last_name, self.candidate.email,
                                                       self.candidate.phone)

    class Meta:
        ordering = ['-event']


class EventJob(models.Model):
    event = models.ForeignKey(Event)
    job_posting = models.ForeignKey(JobPosting)

    def __str__(self):
        return "Event: {0} : {1}".format(self.event.name, self.job_posting.title)

    class Meta:
        ordering = ['-event']
