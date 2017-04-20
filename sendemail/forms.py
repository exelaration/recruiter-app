from django import forms
from django.forms import inlineformset_factory
from .models import EmailTemplate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, HTML


class SendEmailForm(forms.Form):
    error_css_class = 'errorlist'

    email_templates = forms.ChoiceField(label='Choose Email Template to use', initial='', required=True)

    class Meta:
        model = EmailTemplate

    def __init__(self, *args, **kwargs):
        super(SendEmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_id = 'id-registrationForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.form_action = 'detail'
        self.helper.layout = Layout(
            Fieldset(
                'Choose Email Template',
                'email_templates',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-default')
            )
        )
