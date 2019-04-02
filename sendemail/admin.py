from django.contrib import admin

import sendemail.models.email_log
import sendemail.models.email_template


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['subject', 'enabled']
    fields = ['subject', 'body', 'enabled']
    search_fields = ['subject', 'enabled']
    list_filter = ['subject', 'enabled']


class EmailLogAdmin(admin.ModelAdmin):
    list_display = ['time_sent', 'event_id', 'candidate_id', 'to_address', 'from_address', 'subject', 'response']
    search_fields = ['time_sent', 'event_id', 'candidate_id', 'to_address', 'from_address', 'subject', 'body', 'response']
    list_filter = ['time_sent', 'event_id', 'candidate_id', 'to_address', 'from_address', 'subject']


admin.site.register(sendemail.models.email_template.EmailTemplate, EmailTemplateAdmin)
admin.site.register(sendemail.models.email_log.EmailLog, EmailLogAdmin)
