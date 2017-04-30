from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_time', 'enabled']
    fields = ['date_time', 'title', 'job_postings', 'enabled']


class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'job_link', 'enabled']
    fields = ['title', 'location', 'job_link', 'enabled']


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'phone']
    fields = ['first_name', 'last_name', 'email', 'phone']


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.JobPosting, JobPostingAdmin)
admin.site.register(models.Candidate, CandidateAdmin)
admin.site.register(models.Attendance)

