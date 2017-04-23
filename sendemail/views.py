from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from sendemail.forms import SendEmailForm
from .models import EmailTemplate
from events.models import Event, Attendance



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
            send_emails(request, form, event_id)
            return HttpResponseRedirect('/sendemail')

    else:  # if a GET (or any other method) we'll create a blank form
        form = SendEmailForm()
        form.fields['email_templates'].choices = get_all_active_email_templates()
        return render(request, 'sendemail/detail.html', {'event': event,
                                                         'attendance_list': attendance_list,
                                                         'form': form})


def get_all_active_email_templates():
    return [(email_template.id, str(email_template)) for email_template in EmailTemplate.objects.filter(enabled=True)]


def send_emails(request, form, event_id):
    pass

