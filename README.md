# FullThrottle
Django Project to design and implement a Django application with User and ActivityPeriod models, write a custom management command to populate the database with some dummy data, and design an API to serve that data in the json format.


# Project Setup
-> pip install django
-> django-admin startproject FullThrottle


# Execution commands
-> python manage.py startapp activity


# Make migrations to Django db
-> python manage.py makemigrations
-> python manage.py migrate

# Create a super user
-> python manage.py createsuperuser

# Run the project
-> python manage.py runserver

# API to fetch data from Django
-> localhost/activityPeriod

# Persist data in Django
-> python manage.py loaddata static_json.json