from django.contrib import admin
from . import models


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['subject', 'enabled']
    fields = ['subject', 'body', 'enabled']
    search_fields = ['subject', 'enabled']
    list_filter = ['subject', 'enabled']


class EmailLogAdmin(admin.ModelAdmin):
    list_display = ['time_sent', 'event_id', 'candidate_id', 'to_address', 'from_address', 'subject']
    fields = ['time_sent', 'event_id', 'candidate_id', 'to_address', 'from_address', 'subject', 'body', 'response']
    search_fields = ['time_sent', 'event_id', 'candidate_id', 'to_address', 'from_address', 'subject', 'body', 'response']
    list_filter = ['time_sent', 'event_id', 'candidate_id', 'to_address', 'from_address', 'subject']


admin.site.register(models.EmailTemplate, EmailTemplateAdmin)
admin.site.register(models.EmailLog, EmailLogAdmin)
