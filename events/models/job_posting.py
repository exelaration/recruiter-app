from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html


class JobPosting(models.Model):
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=100, blank=True, null=True)
    job_link = models.URLField('Job Link', max_length=500)
    enabled = models.BooleanField(default=True)

    def show_job_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.job_link)

    show_job_url.short_description = "Job URL"

    def __str__(self):
        if self.location is None or self.location == '':
            return self.title
        else:
            return "{0} ({1})".format(self.title, self.location)
