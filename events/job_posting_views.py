from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import json

from .models.job_posting import JobPosting
from .form.job_posting import JobPostingForm

def index(request):
    job_posting_list = JobPosting.objects.order_by('-enabled', 'id')
    context = {'job_posting_list': job_posting_list, 'has_jobs': len(job_posting_list) > 0 }
    return render(request, 'events/jp_index.html', context)

def edit(request, job_posting_id):
    if job_posting_id:
        job_posting = get_object_or_404(JobPosting, pk=job_posting_id)
    else:
        job_posting = None

    if request.method == 'POST':  # if this is a POST request we need to process the form data
        form = JobPostingForm(request.POST)
        if form.is_valid():
            update_or_create_template(request, form, job_posting_id)
            response = {'status': 301, 'location': 'postings'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        else:
            return render(request, 'events/jp_modal.html', {'job_posting': job_posting, 'form': form})
    else:
        form = JobPostingForm()

        if job_posting_id is not None:
            form.fields['title'].initial = job_posting.title
            form.fields['location'].initial = job_posting.location
            form.fields['job_link'].initial = job_posting.job_link
            form.fields['enabled'].initial = job_posting.enabled

        return render(request, 'events/jp_modal.html', {'job_posting': job_posting, 'form': form})

def update_or_create_template(request, form, job_posting_id):
    f_title = form.cleaned_data['title']
    f_location = form.cleaned_data['location']
    f_job_link = form.cleaned_data['job_link']
    f_enabled = form.cleaned_data['enabled']

    if job_posting_id is None:
         job_posting = JobPosting(title=f_title, location=f_location, job_link=f_job_link, enabled=f_enabled)
    else:
        job_posting = JobPosting.objects.get(id=job_posting_id)
        job_posting.title = f_title
        job_posting.location = f_location
        job_posting.job_link = f_job_link
        job_posting.enabled = f_enabled

    return job_posting.save()
