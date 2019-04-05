# Todo-App

## Website demo
Todo App[https://todo-app2.herokuapp.com/]
## Dependencies
* Python 3.6
* Django 2.0.5
* PostgreSQL 10
* psycopg2
* psycopg2-binary

This is a simple todo web app, where a user can
* create his everyday schedule,
* edit the schedule by clicking on todo task description/name
* see his schedules
* delete the task from his schedule
 
Additional features are:
* A user can mark his schedule complete(done) or incomplete(not done). 

## Running the website
To run the app, you need to connect to postgresql database on the backend.the steps are:
1. create a postgresql database named "btredb" with owner "postgres".
2. In todo/settings.py, under the DATABASES section, you need to edit the 'PASSWORD'(In the folder, it is 123456, you need to change it to whatever password you set for your btredb database).
3.run this command ```python manage.py runserver ```

## sample images
