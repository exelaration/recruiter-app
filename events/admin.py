from django.contrib import admin

from events.models.attendance import Attendance
from events.models.candidate import Candidate
from events.models.event import Event
from events.models.job_posting import JobPosting


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_time', 'enabled']
    fields = ['date_time', 'title', 'job_postings', 'enabled', 'auto_email', 'auto_email_from', 'email_template']
    search_fields = ['title', 'date_time', 'enabled']
    list_filter = ['date_time', 'enabled']


class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'job_link', 'enabled']
    fields = ['title', 'location', 'job_link', 'enabled']
    search_fields = ['title', 'location', 'job_link', 'enabled']
    list_filter = ['location', 'enabled']

    ## Remove delete selected option from list of job postings
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    ## Disallow delete by anyone of job postings -- no delete button on job posting edit page
    def has_delete_permission(self, request, obj=None):
        return False

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'phone']
    fields = ['first_name', 'last_name', 'email', 'phone']
    search_fields = ['last_name', 'first_name', 'email', 'phone']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'event_title', 'candidate_first_name', 'candidate_last_name',
                    'candidate_email', 'candidate_phone', 'selected_job_posting']
    search_fields = ['event__title', 'candidate__first_name', 'candidate__last_name',
                     'candidate__email', 'candidate__phone', 'selected_job_posting']
    list_filter = ['event__title', 'selected_job_posting']

    def event_id(self, obj):
        return obj.event.id

    def event_title(self, obj):
        return obj.event.title

    def candidate_first_name(self, obj):
        return obj.candidate.first_name

    def candidate_last_name(self, obj):
        return obj.candidate.last_name

    def candidate_email(self, obj):
        return obj.candidate.email

    def candidate_phone(self, obj):
        return obj.candidate.phone

    def selected_job_posting(self, obj):
        return obj.selected_job_posting


admin.site.register(Event, EventAdmin)
admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Attendance, AttendanceAdmin)
