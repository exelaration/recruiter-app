# Recruit
##### Recruit web app for Excella NEST project
* Use this web app to gather contact information from possible recruits and later send email with a link to job posting they are interested in
* Information we want to gather:
    * First Name (Required)
    * Last Name (Required)
    * Phone Number (Optional)
    * Email Address (Required)
* Use above information to send out emails to all applicants a reminder to apply online

# Recruiter
1. Uses admin console to add Job Postings 
2. Create new event/career fair's
3. Associates 1 or more Job posting (links) with that page
4. Publishes the page and heads to a career fair
5. On 1 or more devices he loads the page for that Carreer fair
6. Attendee uses the page to enter their information (mentioned above)


### Technical Information
This repo was created following an Heroku - DJANGO tutorial:
* https://devcenter.heroku.com/articles/deploying-python

### Steps to work with this repo:
1. Verify supported technology is installed:
    * Python 3.5.x
    * Django
    * Postgres (Database)
    * Whitenoise (For static files)
    * See requirements.txt for full details here
2. Clone the repo
3. Create Virtualenv (steps for CMD console)
    * `$ virtualenv venv` (One time only)
    * `$ venv\Scripts\activate.bat`
    * `$ pip install -r requirements.txt`
4. Create postgresDb
    * Update base.py with Database credentials
    * Usefull ORM commands:
        * `$ python manage.py makemigrations`
        * `$ python manage.py migrate`
        * `$ python manage.py migrate app_name_like_home 0002`
    
### Working with Heroku
* Verify you have the heroku remote:
    * `https://git.heroku.com/excellarecruit.git`
    * `$ heroku login`
    * `$ heroku create` (actually creates the heroku remote)
    * `$ git push heroku master`
* Other useful Heroku commands
    * `$ heroku open`
    * `$ heroku plugins:install heroku-config`
    * `$ heroku config:push`
    * `$ heroku run ...`
    * `$ heroku run python manage.py migrate`
    * `$ heroku run python manage.py createsuperuser`
    * `$ heroku ps:scale web=1`
    * `$ heroku config:get SECRET_KEY`
    * `$ heroku config:set DJANGO_SETTINGS_MODULE=recruit.settings.production`
    * `$ heroku logs --tail --ps postgres --app excellarecruit`
