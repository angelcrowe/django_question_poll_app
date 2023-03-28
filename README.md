# Django Poll App
My first Django app 

---

## About 

This is an official [Django tutorial project](https://docs.djangoproject.com/en/4.1/intro/tutorial01/) 
made to learn the Django framework. Which is a Python-based free and open-source web framework.

--- 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites
`python== 3.5 or up and django==3.0 or up`

#### Installing
> open terminal and type

`git clone https://github.com/angelcrowe/django_question_poll_app.git`

#### To migrate the database open terminal in project directory and type
```
python manage.py makemigrations
python manage.py migrate
```

#### To use admin panel you need to create superuser using this command 
`python manage.py createsuperuser`

#### To run the program in local server use the following command 
`python manage.py runserver`

#### Then go to [LocalHost](http://127.0.0.1:8000/polls) in your browser
