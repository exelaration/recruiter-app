from django.test import TestCase
from django.urls import reverse

from events.models.event import Event
from events.models.job_posting import JobPosting


class RegistrationFormTest(TestCase):
    def setUp(self):
        job_posting = JobPosting.objects.create(title='Do this', job_link='www.excella.com')
        event = Event.objects.create(title = '',
                                     date_time = '01-01-1970 00:00:00', # Needs real date
                                     enabled = True,
                                     job_postings = job_posting,
                                     auto_email = False)

    def test_get_registration_form(self):
        url = reverse("events.views.detail")+'/'+event.id
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("content to look for - is this actually a good idea?", response.content)

    # TODO: test anything that should be pre-populated in specific circumstances


    # TODO: Test post request on /events/num: Attendance is added
    # TODO
    def test_post_valid_registration_form(self):
        pass

    # TODO: one or more tests per registration field - maybe in test_forms.py instead?
    def test_registration_form_invalid_for_each_field(self):
        pass

# TODO: Test get_job_postings_for_event
# TODO: Test update_or_create_candidate

# TODO: Test that emails autosend when someone registers without logging in
#   Check the most recent log against what was expected, or even better find
#   a way to make sure the log is the right one for this registration attempt
