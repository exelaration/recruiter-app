from django import forms
from django.forms import inlineformset_factory
from django.core.validators import RegexValidator
from .models import Candidate, JobPosting, Attendance
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, ButtonHolder, Fieldset, HTML, Button, Row, Field


class RegisterForm(forms.Form):
    candidate_first_name = forms.CharField(label='Your First Name', max_length=200)
    candidate_last_name = forms.CharField(label='Your Last Name', max_length=200)
    candidate_email = forms.EmailField(label='Your Email', max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                 message='Phone number must be entered in the format: ''+999999999''. Up to 15 digits allowed.')
    candidate_phone = forms.CharField(validators=[phone_regex], label='Your Phone Number', max_length=15, required=False)
    JobPostingFormSet = inlineformset_factory(JobPosting, Attendance, fields=('selected_job_posting',))
    candidate_job_posting = forms.ChoiceField(label='Choose Job', initial='', required=True)
