from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Event, Candidate, JobPosting, Attendance
from .forms import RegisterForm

from django.core.validators import validate_email


def index(request):
    event_list = Event.objects.filter(enabled=True).order_by('-date_time')
    context = {'event_list': event_list}
    return render(request, 'events/index.html', context)

def all_events(request):
    event_list = Event.objects.filter(enabled=True).order_by('-date_time')
    events_serialized = serializers.serialize('json', event_list).replace("\'", '"')
    print (events_serialized)
    return JsonResponse(events_serialized, safe=False)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':  # if this is a POST request we need to process the form data
        form = RegisterForm(request.POST)
        form.fields['candidate_job_posting'].choices = get_job_postings_for_event(event_id)
        if form.is_valid():
            candidate_email = update_or_create_candidate(request, form, event_id)
            context = {'candidate_email': candidate_email, 'event': event}
            return render(request, 'events/registration_complete.html', context)
        else:
            return render(request, 'events/detail.html', {'event': event, 'form': form})

    else:  # if a GET (or any other method) we'll create a blank form
        form = RegisterForm()
        form.fields['candidate_job_posting'].choices = get_job_postings_for_event(event_id)
        return render(request, 'events/detail.html', {'event': event, 'form': form})

    return render(request, 'events/detail.html', {'event': event, 'form': form})


def get_job_postings_for_event(event_id):
    return [(job_posting.id, str(job_posting)) for job_posting in JobPosting.objects.filter(enabled=True).filter(event__id=event_id)]


def update_or_create_candidate(request, form, event_id):
    f_email = form.cleaned_data['candidate_email']
    f_first_name = form.cleaned_data['candidate_first_name']
    f_last_name = form.cleaned_data['candidate_last_name']
    f_phone = form.cleaned_data['candidate_phone']
    job_posting_id = request.POST.getlist('candidate_job_posting')[0]
    f_selected_job_posting = JobPosting.objects.get(id=job_posting_id)
    event_attended = Event.objects.get(id=event_id)
    person = Candidate.objects.filter(email=f_email).first()

    if person is None:
        person = Candidate(first_name=f_first_name, last_name=f_last_name, email=f_email, phone=f_phone)
    else:
        person.first_name = f_first_name
        person.last_name = f_last_name
        person.phone = f_phone

    person.save()

    attendance = Attendance.objects.filter(candidate=person).filter(event=event_attended).filter(selected_job_posting=f_selected_job_posting).first()
    if attendance is None:
        attendance = Attendance(candidate=person, event=event_attended, selected_job_posting=f_selected_job_posting)
        attendance.save()

    return f_email

