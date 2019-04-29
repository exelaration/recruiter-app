from django import forms
from tinymce.widgets import TinyMCE
from ..models.job_posting import JobPosting

class JobPostingForm(forms.Form):
    title = forms.CharField(max_length=300, required=True)
    location = forms.CharField(max_length=100, required=False)
    job_link = forms.CharField(label='Job Link', max_length=500, required=True)
    enabled = forms.BooleanField(required=False)

    class Meta:
        model = JobPosting
        fields = '__all__'
