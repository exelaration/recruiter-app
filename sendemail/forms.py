from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from django import forms

from sendemail.models.email_template import EmailTemplate


class SendEmailForm(forms.Form):
    error_css_class = 'errorlist'

    email_templates = forms.ChoiceField(label='Email Template', initial='', required=True)

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
        )
