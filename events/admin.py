from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_time', 'enabled']
    fields = ['enabled', 'date_time', 'name', 'description']


class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_link', 'description']
    fields = ['title', 'job_link', 'description']


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'phone']


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Candidate, CandidateAdmin)
admin.site.register(models.Application)
admin.site.register(models.JobPosting)
