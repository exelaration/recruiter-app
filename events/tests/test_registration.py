from django.test import TestCase
from events.forms import RegisterForm

# Create your tests here.

# TODO: Test that emails autosend when someone registers without logging in

class RegisterFormTest(TestCase):
    def test_RegisterForm_invalid_when_missing_all_data(self):
        form = RegisterForm()
        self.assertFalse(form.is_valid())

    def test_RegisterForm_invalid_when_missing_last_name(self):
        form = RegisterForm(data={
            'candidate_first_name' : 'Joe'
        })
        self.assertEqual(form['candidate_first_name'].value(), 'Joe')
        self.assertFalse(form.is_valid())

    def test_RegisterForm_invalid_when_missing_email(self):
        form = RegisterForm(data={
            'candidate_first_name' : 'Joe',
            'candidate_last_name' : 'Developer'
        })
        self.assertEqual(form['candidate_first_name'].value(), 'Joe')
        self.assertEqual(form['candidate_last_name'].value(), 'Developer')
        self.assertFalse(form.is_valid())

    def test_RegisterForm_invalid_when_missing_phone(self):
        form = RegisterForm(data={
            'candidate_first_name' : 'Joe',
            'candidate_last_name' : 'Developer',
            'candidate_email' : 'Joe.Developer@excella.com'
        })
        self.assertEqual(form['candidate_first_name'].value(), 'Joe')
        self.assertEqual(form['candidate_last_name'].value(), 'Developer')
        self.assertEqual(form['candidate_email'].value(), 'Joe.Developer@excella.com')
        self.assertFalse(form.is_valid())

    def test_RegisterForm_invalid_when_phone_invalid(self):
        form = RegisterForm(data={
            'candidate_first_name' : 'Joe',
            'candidate_last_name' : 'Developer',
            'candidate_email' : 'Joe.Developer@excella.com',
            'candidate_phone' : '703-ABC-DEFG'
        })
        self.assertEqual(form['candidate_first_name'].value(), 'Joe')
        self.assertEqual(form['candidate_last_name'].value(), 'Developer')
        self.assertEqual(form['candidate_email'].value(), 'Joe.Developer@excella.com')
        self.assertEqual(form['candidate_phone'].value(), '703-ABC-DEFG')
        self.assertFalse(form.is_valid())
        phoneRegexMsg = form.phone_regex.message
        self.assertTrue(form.errors['candidate_phone'].as_text().find(phoneRegexMsg) >= 0)

    def test_RegisterForm_invalid_when_missing_job_postings(self):
        form = RegisterForm(data={
            'candidate_first_name' : 'Joe',
            'candidate_last_name' : 'Developer',
            'candidate_email' : 'Joe.Developer@excella.com',
            'candidate_phone' : '703-123-4567'
        })
        self.assertEqual(form['candidate_first_name'].value(), 'Joe')
        self.assertEqual(form['candidate_last_name'].value(), 'Developer')
        self.assertEqual(form['candidate_email'].value(), 'Joe.Developer@excella.com')
        self.assertEqual(form['candidate_phone'].value(), '703-123-4567')
        self.assertFalse(form.is_valid())
