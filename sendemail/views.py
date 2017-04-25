from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from sendemail.forms import SendEmailForm
from .models import EmailTemplate
from events.models import Event, Attendance

import os
import sendgrid
from sendgrid.helpers.mail import *


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
            send_emails(request, event, attendance_list)
            return HttpResponseRedirect('/sendemail')

    else:  # if a GET (or any other method) we'll create a blank form
        form = SendEmailForm()
        form.fields['email_templates'].choices = get_all_active_email_templates()
        return render(request, 'sendemail/detail.html', {'event': event,
                                                         'attendance_list': attendance_list,
                                                         'form': form})


def get_all_active_email_templates():
    return [(email_template.id, str(email_template)) for email_template in EmailTemplate.objects.filter(enabled=True)]


@login_required
def send_email(from_address, to_address, subject, body_text):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(from_address)
    to_email = Email(to_address)
    content = Content("text/plain", body_text)
    current_email = Mail(from_email, subject, to_email, content)

    response = sg.client.mail.send.post(request_body=current_email.get())
    return response


@login_required
def send_test_email(request, event_id, attendance_id):
    
    print('#########################################')
    print('#########################################')
    print('Logged In User: ' + str(request.user))
    print(request.user.username)
    print(request.user.first_name)
    print(request.user.last_name)
    print(request.user.email)
    print('event_id: ' + event_id)
    print('attendance_id: ' + attendance_id)
    print('#########################################')
    print('#########################################')
    return HttpResponseRedirect('/sendemail/{event_id}'.format(event_id=event_id))


@login_required
def send_emails(request, event, attendance_list):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("allen.tuggle@excella.com")
    to_email = Email("allen.tuggle@excella.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")

    # current_email = Mail(from_email, subject, to_email, content)
    #
    # response = sg.client.mail.send.post(request_body=current_email.get())
    print('#########################################')
    print('#########################################')
    print('Logged In User: ' + str(request.user))
    print(request.user.username)
    print(request.user.first_name)
    print(request.user.last_name)
    print(request.user.email)
    print('#########################################')
    print('#########################################')
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)
    # print('#########################################')
    # print('#########################################')
