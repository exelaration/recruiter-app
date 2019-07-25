from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from sendemail.models.email_template import EmailTemplate
from .form.email_template import TemplateForm

def index(request):
    email_template_list = EmailTemplate.objects.order_by('-enabled', 'id')
    context = {'email_template_list': email_template_list, 'has_templates': len(email_template_list) > 0 }
    return render(request, 'events/et_index.html', context)

def edit(request, template_id):
    saved = False
    if template_id:
        email_template = get_object_or_404(EmailTemplate, pk=template_id)
    else:
        email_template = None

    if request.method == 'POST':  # if this is a POST request we need to process the form data
        form = TemplateForm(request.POST)
        if form.is_valid():
            update_or_create_template(request, form, template_id)
            saved = True

    else:
        form = TemplateForm()

        if template_id is not None:
            form.fields['subject'].initial = email_template.subject
            form.fields['body'].initial = email_template.body
            form.fields['enabled'].initial = email_template.enabled

    if not saved:
        return render(request, 'events/et_modal.html', {'email_template': email_template, 'form': form})
    else:
        return render(request, 'events/et_saved.html')


def update_or_create_template(request, form, template_id):
    f_subject = form.cleaned_data['subject']
    f_body = form.cleaned_data['body']
    f_enabled = form.cleaned_data['enabled']

    if template_id is None:
         template = EmailTemplate(subject=f_subject, body=f_body, enabled=f_enabled)
    else:
        template = EmailTemplate.objects.get(id=template_id)
        template.subject = f_subject
        template.body = f_body
        template.enabled = f_enabled

    return template.save()
