from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Event, Candidate, JobPosting
from .forms import RegisterForm

from django.core.validators import validate_email


def index(request):
    event_list = Event.objects.filter(enabled=True).order_by('-date_time')
    context = {'event_list': event_list}
    return render(request, 'events/index.html', context)


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':  # if this is a POST request we need to process the form data
        form = RegisterForm(request.POST)
        if form.is_valid():
            update_or_create_candidate(form)
            return HttpResponseRedirect('/events/{0}'.format(event_id))

    else:  # if a GET (or any other method) we'll create a blank form
        form = RegisterForm()
        # form.fields['job_posting'].choices = JobPosting.objects.filter(event_id=event_id)  # Filter EventJob's where event_id = event_id and then return all job_links
        return render(request, 'events/detail.html', {'event': event, 'form': form})

    return render(request, 'events/detail.html', {'event': event, 'form': form})


def update_or_create_candidate(form):
    f_email = form.cleaned_data['candidate_email']
    f_first_name = form.cleaned_data['candidate_first_name']
    f_last_name = form.cleaned_data['candidate_last_name']
    f_phone = form.cleaned_data['candidate_phone']
    f_selected_job_posting = form.cleaned_data['candidate_job_posting']
    p = Candidate.objects.filter(email=f_email).first()

    if p is None:
        p = Candidate(first_name=f_first_name, last_name=f_last_name, email=f_email, phone=f_phone, selected_job_posting=f_selected_job_posting)
    else:
        p.first_name = f_first_name
        p.last_name = f_last_name
        p.phone = f_phone
        p.job_posting = f_selected_job_posting

    p.save()
