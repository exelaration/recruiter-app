from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ['enabled', 'title', 'date_time']
    fields = ['enabled', 'date_time', 'title', 'job_postings']


class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'job_link']
    fields = ['title', 'location', 'job_link']


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'phone', 'selected_job_posting']
    fields = ['first_name', 'last_name', 'email', 'phone', 'selected_job_posting']


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Candidate, CandidateAdmin)
admin.site.register(models.JobPosting, JobPostingAdmin)
