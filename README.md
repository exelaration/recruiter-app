# Recruit
Currently deployed here: https://excella-jobs-stg.herokuapp.com/events/
##### Excella Jobs Web App for Recruiting
* Use this web app to gather contact information from possible recruits and later send email with a link to job posting they are interested in
* Information we want to gather:
    * First Name (Required)
    * Last Name (Required)
    * Phone Number (Optional)
    * Email Address (Required)
    * Selected Job Posting (Required)
* An email will be sent to the applicant upon completion of this form based on an associated template

# Recruiter
1. Uses admin console to add Job Postings 
2. Create new event/career fair's
3. Create one or more Job postings for related to event
4. Associates 1 or more Job posting (links) with that page
5. Create an Email template for related evevnt used for sending candidate email
6. Associate Email template with the new event
7. Publishes the page and heads to a career fair
8. On 1 or more devices he loads the page for that Carreer fair
9. Candidate uses the page to enter their information (mentioned above)


### Technical Information
This Web App is build using Python Django back end and an Angular 5 front end.
It is a mixture of Django RESTfull api in the back end plus Django admin for managing models

### Steps to work with this repo:
1. Verify that the following are installed:
    * Git
    * Docker
2. Create an SSH public-private key pair for Git
3. Clone the repository from GitHub
    * On Windows, ensure that git will check out files with line endings as-is `git config --global core.autocrlf input`
4. Run Docker files for running this app locally
    * `$ docker-compose up -d` (One time only)
        * NOTE: If running docker on OSX you will need to turn on `securely store Docker logins in macOS keychain` under docker preferences.  For more info see: https://github.com/ansible/ansible-container/issues/722
    * Run this command to create db superuser for admin console:
        * `$ docker-compose exec web python manage.py createsuperuser`
        * I tend to use 'admin' as my user name
5. Access the website at `http://localhost:8000/events/` and `http://localhost:8000/admin/` 
6. Useful when troubleshooting:
    * `docker-compose exec web [command]` into docker container to run the below commands
    * Update base.py with Database credentials
    * Usefull ORM commands:
        * `$ python manage.py makemigrations` - run after database ("model") changes
        * `$ python manage.py migrate` - run after `makemigrations` or fetching new 
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

## Heroku Instructions for working with this Project:
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

    $ heroku login

Clone the repository

Use Git to clone excellajobs's source code to your local machine.

    $ heroku git:clone -a excellajobs
    $ cd excellajobs
    
Deploy your changes

Make some changes to the code you just cloned and deploy them to Heroku using Git.

    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master
