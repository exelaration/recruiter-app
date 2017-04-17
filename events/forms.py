from django import forms
from django.forms import inlineformset_factory
from .models import Candidate, JobPosting
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, HTML


class RegisterForm(forms.Form):
    error_css_class = 'errorlist'

    candidate_first_name = forms.CharField(label='Your First Name', max_length=200)
    candidate_last_name = forms.CharField(label='Your Last Name', max_length=200)
    candidate_email = forms.EmailField(label='Your Email', max_length=200)
    candidate_phone = forms.CharField(label='Your Phone Number', max_length=15, required=False)
    JobPostingFormSet = inlineformset_factory(JobPosting, Candidate, fields=('selected_job_posting',))
    candidate_job_posting = forms.ChoiceField(label='Job Postings', initial='', required=True)

    class Meta:
        model = Candidate

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_id = 'id-registrationForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.form_action = 'detail'
        self.helper.layout = Layout(
            Fieldset(
                'Please Register',
                'candidate_first_name',
                'candidate_last_name',
                'candidate_email',
                'candidate_phone',
                'candidate_job_posting',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-default')
            )
        )
        # self.helper.add_input(Submit('submit', 'Submit'))
