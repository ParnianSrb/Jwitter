# Jwitter
### The idea is to create a website similar to Twitter!, and it is Jwitter because because of the Django framework :D
#### In order to learn Python in different branches, I decided to build an easy website with Django 

#### Description:
We need a Database to store the information about Posts, we need Username and Password to login and be able to create posts.

#### Details: 
1. Libraries exist in my Virtual Environment - the "requirements.txt" file contains the libraries
2. Django can start an Admin System right away by this code in our project folder when virtual environment is active:
   ... (venv)jwitter> django-admin startproject jwitter  # my main folder and project folder names are both "jwitter"
   by this code, we will see that in our main folder there are two things: 1)jwitter folder, which is the project folder  2)a file "manage.py"
4. I name my Django app "blog" in the project folder -this process is done by using "manage.py" file which was self-created when I started my project-
   ... (venv)jwitter/jwitter> python manage.py startapp blog
5. To start the server:
   ... (venv)jwitter/jwitter> python manage.py runserver  # the outcome link only shows the standard Django website
6. Django is an MVC model (Model: Info in the DB, View: What can be seen, Controller: How developer Connects Model and View)
   this is because we have some files in the blog app, namely: model.py, views.py, urls.py)
7. Then we create our Views and the Urls of our Views in the blog app, one more thing is to add these Urls from blog to the original project Urls file in jwitter
   To do this we need to import path and include from django.urls in the "urls.py" file of jwitter project
8. Now blog page and admin page are ready to be seen after running the server.
  
