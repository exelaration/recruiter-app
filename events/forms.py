from django import forms
from django.core.validators import RegexValidator
from django.forms import inlineformset_factory

from events.models.attendance import Attendance
from events.models.job_posting import JobPosting

from sendemail.models.email_template import EmailTemplate

class RegisterForm(forms.Form):
    candidate_first_name = forms.CharField(label='First name:', max_length=50)
    candidate_last_name = forms.CharField(label='Last name:', max_length=50)
    candidate_email = forms.EmailField(label='Email:', max_length=200)
    phone_regex = RegexValidator(regex=r'^\d{3}-\d{3}-\d{4}$',
                                 message='Phone number must be entered in the format: \'123-123-1234\'.')
    candidate_phone = forms.CharField(validators=[phone_regex], label='Phone number:', max_length=12, required=False, widget=forms.TextInput(attrs={'placeholder': 'XXX-XXX-XXXX'}))
    JobPostingFormSet = inlineformset_factory(JobPosting, Attendance, fields=('selected_job_posting',))
    candidate_job_postings = forms.MultipleChoiceField(label='Jobs:', initial='', widget=forms.SelectMultiple(), required=True)

class EventForm(forms.Form):
    event_date = forms.DateField(label='Event date', widget=forms.TextInput(attrs={'autocomplete':'off'}))
    event_title = forms.CharField(label='Title of Event')
    event_jobs = forms.MultipleChoiceField(label='Job postings', initial='', widget=forms.SelectMultiple(), required=True)
    event_auto_send = forms.BooleanField(label='Auto send email on registration', required=False)
    event_sender = forms.EmailField(label='Auto-email sender', max_length=200, required=False)
    templateChoices = [('','')] + [(email_template.id, str(email_template)) for email_template in
                 EmailTemplate.objects.filter(enabled=True)]
    event_default_template = forms.ChoiceField(label='Default email template', choices=templateChoices, required=False)
