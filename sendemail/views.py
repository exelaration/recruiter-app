from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from sendemail.forms import SendEmailForm
from .models import EmailTemplate
from sendemail.xlsx_formatter import *
from events.models import Event, Attendance

import os
import sendgrid
from sendgrid.helpers.mail import *


@login_required
def exportXlsx(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    file_name = "Attendee_List_Event_{0}.xlsx".format(event.id)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(file_name)

    attendance_list = Attendance.objects.filter(event=event)
    xlsx_data = writeToExcel(attendance_list, event)
    response.write(xlsx_data)
    return response


@login_required
def index(request):
    event_list = Event.objects.filter(enabled=True).order_by('-date_time')
    context = {'event_list': event_list}
    return render(request, 'sendemail/index.html', context)


@login_required
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendance_list = Attendance.objects.filter(event=event)

    if request.method == 'POST':  # if this is a POST request we need to process the form data
        form = SendEmailForm(request.POST)
        form.fields['email_templates'].choices = get_all_active_email_templates()
        if form.is_valid():
            email_template_id = request.POST.getlist('email_templates')[0]
            email_template = EmailTemplate.objects.get(id=email_template_id)
            send_emails(request, email_template, attendance_list, event)
            return HttpResponseRedirect('/sendemail')

    else:  # if a GET (or any other method) we'll create a blank form
        form = SendEmailForm()
        form.fields['email_templates'].choices = get_all_active_email_templates()
        return render(request, 'sendemail/detail.html', {'event': event,
                                                         'attendance_list': attendance_list,
                                                         'form': form})


def get_all_active_email_templates():
    return [(email_template.id, str(email_template)) for email_template in EmailTemplate.objects.filter(enabled=True)]


def send_emails(request, email_template, attendance_list, event):
    from_email = str(request.user.email)
    candidates_to_job_postings = []
    for attendance in attendance_list:
        candidates_to_job_postings[attendance.candidate] += [attendance.selected_job_posting]
    for candidate, job_postings in candidates_to_job_postings:
        to_email = str(candidate.email)
        subject = str(email_template.subject)
        email_body = email_template.body.replace('##FIRST_NAME##', candidate.first_name)
        email_body = email_body.replace('##LAST_NAME##', candidate.last_name)
        email_body = email_body.replace('##EVENT##', event.title)
        email_body = email_body.replace('##JOBPOSTING##', job_postings[0].)
        email_body = email_body.replace('##JOBPOSTING##', job_postings[0].job_link)
        response = send_email(from_email, to_email, subject, str(email_body))
        print(response)


def send_email(from_address, to_address, subject, body_text):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(from_address)
    to_email = Email(to_address)
    content = Content("text/html", body_text)
    current_email = Mail(from_email, subject, to_email, content)
    print('#############################')
    print('Send Email {0} : {1}'.format(to_address, subject))
    print('#############################')
    response = sg.client.mail.send.post(request_body=current_email.get())
    return response
