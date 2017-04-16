from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Event, Candidate, Application
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
            p_id = get_candidate_id(form)
            candidate_record = Application.objects.filter(candidate_id=p_id).first()

            print('################')
            print('p_id: ' + str(p_id) + " ### " + str(candidate_record))
            print('################')

            if candidate_record is None:
                print('=========================')
                print('Inside create application')
                print('=========================')
                attend = Application(candidate_id=p_id, event_id=event_id)
                attend.save()
                print('Saved application')

            return HttpResponseRedirect('/events/{0}'.format(event_id))

    else:  # if a GET (or any other method) we'll create a blank form
        form = RegisterForm()
        return render(request, 'events/detail.html', {'event': event, 'form': form})

    return render(request, 'events/detail.html', {'event': event, 'form': form})


def get_candidate_id(form):
    f_email = form.cleaned_data['candidate_email']
    f_first_name = form.cleaned_data['candidate_first_name']
    f_last_name = form.cleaned_data['candidate_last_name']
    f_phone = form.cleaned_data['candidate_phone']
    p = Candidate.objects.filter(email=f_email).first()

    if p is None:
        p = Candidate(first_name=f_first_name, last_name=f_last_name, email=f_email, phone=f_phone)
    else:
        p.first_name = f_first_name
        p.last_name = f_last_name
        p.phone = f_phone

    p.save()
    return p.id
