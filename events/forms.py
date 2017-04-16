from django import forms
from .models import Candidate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RegisterForm(forms.Form):
    error_css_class = 'errorlist'

    candidate_first_name = forms.CharField(label='Your First Name', max_length=200)
    candidate_last_name = forms.CharField(label='Your Last Name', max_length=200)
    candidate_email = forms.EmailField(label='Your Email', max_length=200)
    candidate_phone = forms.CharField(label='Your Phone Number', max_length=200)

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
