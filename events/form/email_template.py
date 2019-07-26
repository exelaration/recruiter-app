from django import forms
from tinymce.widgets import TinyMCE
from sendemail.models.email_template import EmailTemplate

class TemplateForm(forms.Form):
    subject = forms.CharField(label='Subject:', max_length=100, required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}), required=True)
    enabled = forms.BooleanField(required=False)

    class Meta:
        model = EmailTemplate
        fields = '__all__'
