from django import forms
from django.forms import inlineformset_factory
from .models import Candidate, JobPosting
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RegisterForm(forms.Form):
    error_css_class = 'errorlist'

    helper = FormHelper()
    helper.form_tag = False
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'

    candidate_first_name = forms.CharField(label='Your First Name', max_length=200)
    candidate_last_name = forms.CharField(label='Your Last Name', max_length=200)
    candidate_email = forms.EmailField(label='Your Email', max_length=200)
    candidate_phone = forms.CharField(label='Your Phone Number', max_length=15, required=False)
    JobPostingFormSet = inlineformset_factory(JobPosting, Candidate, fields=('selected_job_posting',))
    candidate_job_posting = forms.ChoiceField(initial='', required=True)

    class Meta:
        model = Candidate

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registrationForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'detail'
        self.helper.add_input(Submit('submit', 'Submit'))
