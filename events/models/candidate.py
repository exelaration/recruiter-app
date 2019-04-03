from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models

from events.models.job_posting import JobPosting


class Candidate(models.Model):
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    email = models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                 message='Phone number must be entered in the format: ''+999999999''. Up to 15 digits allowed.')
    phone = models.CharField(validators=[phone_regex], blank=True,
                             max_length=16, null=True) #validators should be a list
    selected_jobs = models.ManyToManyField(JobPosting, through='Attendance')

    def __str__(self):
        return "{0} {1} - {2}".format(self.first_name, self.last_name, self.email)

    # These permit use as a dictionary key
    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return other and self.id == other.id

    def __ne__(self, other):
        return not(self == other)

    class Meta:
        verbose_name_plural = 'Candidates'
