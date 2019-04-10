from django.test import TestCase


# TODO: Test get request on /events or programmatically pulled URL: registration form is returned
class RegistrationFormTest(TestCase):
    # def setUp(self):
    #     pass

    # TODO
    def test_get_registration_form(self):
        pass

    # TODO: test anything that should be pre-populated in specific circumstances


# TODO: Test post request on /events: Attendance is added
class RegistrationFormTest(TestCase):
    # TODO
    def test_post_valid_registration_form(self):
        pass

    # TODO: one or more per registration field - maybe in test_forms.py instead?
    def test_registration_form_invalid_for_each_field(self):
        pass

# TODO: Test get_job_postings_for_event
# TODO: Test update_or_create_candidate

# TODO: Test that emails autosend when someone registers without logging in
#   Check the most recent log against what was expected, or even better find
#   a way to make sure the log is the right one for this registration attempt
