# testforsucess-api

To run this make sure that you have the OS variable set for heroku DB:
`export SQLALCHEMY_DATABASE_URI=$(heroku config:get DATABASE_URL -a testforsuccess-api)`
The above command requires that you have Heroku CLI installed.

After you initialize the DB variable, from the root folder run:
`gunicorn wsgi:app`

Navigate to:
`localhost:8000/api/<insert controller name>`

Also handles 404, navigate to any other endpoint and you will see a prompt.
