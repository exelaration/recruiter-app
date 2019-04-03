from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from events.models.attendance import Attendance
from events.models.candidate import Candidate
from events.models.event import Event
from events.models.job_posting import JobPosting
from .forms import RegisterForm, EventForm

from django.core.validators import validate_email


def index(request):
    event_list = Event.objects.filter(enabled=True).order_by('-date_time')
    context = {'event_list': event_list}
    return render(request, 'events/index.html', context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':  # if this is a POST request we need to process the form data
        form = RegisterForm(request.POST)
        form.fields['candidate_job_postings'].choices = get_job_postings_for_event(event_id)
        if form.is_valid():
            candidate_email = update_or_create_candidate(request, form, event_id)
            context = {'candidate_email': candidate_email, 'event': event}
            return render(request, 'events/registration_complete.html', context)
        else:
            return render(request, 'events/detail.html', {'event': event, 'form': form})

    else:  # if a GET (or any other method) we'll create a blank form
        form = RegisterForm()
        form.fields['candidate_job_postings'].choices = get_job_postings_for_event(event_id)
        return render(request, 'events/detail.html', {'event': event, 'form': form})

    return render(request, 'events/detail.html', {'event': event, 'form': form})


def edit(request, event_id):
    if event_id:
        event = get_object_or_404(Event, pk=event_id)
    else:
        event = False

    if request.method == 'POST':  # if this is a POST request we need to process the form data
        form = EventForm(request.POST)
        form.fields['event_jobs'].choices = get_all_enabled_job_postings()
        if form.is_valid():
            update_or_create_event(request, form, event_id)
            return redirect('/events')
        else:
            return render(request, 'events/evt_modal.html', {'event': event, 'form': form})

    else:  # if a GET (or any other method) we'll create a blank form
        form = EventForm()
        if event:
            form.fields['event_date'].initial = event.date_time
            form.fields['event_title'].initial = event.title
            form.fields['event_jobs'].choices = get_all_enabled_job_postings()
            form.fields['event_jobs'].initial = get_job_posting_ids_for_event(event_id)
            print (get_job_posting_ids_for_event(event_id))
        else:
            form.fields['event_jobs'].choices = get_all_enabled_job_postings()

        return render(request, 'events/evt_modal.html', {'event': event, 'form': form})


def get_job_postings_for_event(event_id):
    return [(job_posting.id, str(job_posting)) for job_posting in JobPosting.objects.filter(enabled=True).filter(event__id=event_id)]

def get_job_posting_ids_for_event(event_id):
    return [job_posting.id for job_posting in JobPosting.objects.filter(enabled=True).filter(event__id=event_id)]

def get_all_enabled_job_postings():
    return [(job_posting.id, str(job_posting)) for job_posting in JobPosting.objects.filter(enabled=True)]

def update_or_create_candidate(request, form, event_id):
    f_email = form.cleaned_data['candidate_email']
    f_first_name = form.cleaned_data['candidate_first_name']
    f_last_name = form.cleaned_data['candidate_last_name']
    f_phone = form.cleaned_data['candidate_phone']
    job_posting_ids = request.POST.getlist('candidate_job_postings')
    f_selected_job_postings = []
    for job_id in job_posting_ids:
        f_selected_job_postings += [JobPosting.objects.get(id=job_id)]
    event_attended = Event.objects.get(id=event_id)
    person = Candidate.objects.filter(email=f_email).first()

    if person is None:
        person = Candidate(first_name=f_first_name, last_name=f_last_name, email=f_email, phone=f_phone)
    else:
        person.first_name = f_first_name
        person.last_name = f_last_name
        person.phone = f_phone

    person.save()

    for job_posting in f_selected_job_postings:
        attendance = Attendance.objects\
            .filter(candidate=person)\
            .filter(event=event_attended)\
            .filter(selected_job_posting=job_posting)\
            .first()
        if attendance is None:
            attendance = Attendance(candidate=person, event=event_attended, selected_job_posting=job_posting)
            attendance.save()

    return f_email

def update_or_create_event(request, form, event_id):
    print(event_id)
    f_date = form.cleaned_data['event_date']
    f_title = form.cleaned_data['event_title']
    job_posting_ids = request.POST.getlist('event_jobs')
    if event_id is None:
        event = Event(title=f_title, date_time=f_date, enabled=True)
        event.save()
        event.job_postings=job_posting_ids
    else:
        event = Event.objects.get(id=event_id)
        event.title = f_title
        event.date_time = f_date
        event.job_postings = job_posting_ids

    event.save()
    return
