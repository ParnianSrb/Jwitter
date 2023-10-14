# Jwitter
## The idea is to create a website similar to Twitter!, and it is Jwitter because because of the Django framework :D
### In order to learn Python in different branches, I decided to build a simple website with Django 

### Description:
We need a Database to store the information about Posts, we need Username and Password to login and be able to create Posts.

### Details: 
1. I used Virtual Environment and the "requirements.txt" file contains the libraries.
2. Django can start an "Admin System" right away by this code in our project folder, when virtual environment is active:

   ... (venv)jwitter> django-admin startproject jwitter  # my main folder and project folder names are both "jwitter"
   
   by this code, we will see that in our main folder there are two things: 1)jwitter folder, which is the project folder  2)"manage.py" file
   
3. I name my Django app "blog" in the project folder -this process is done by using "manage.py" file (we can run django commands via manage.py)  which was self-created when I started my project-
   
   ... (venv)jwitter/jwitter> python manage.py startapp blog
   
4. To start the server:
   
   ... (venv)jwitter/jwitter> python manage.py runserver  # the outcome link only shows the standard Django website
   
5. Django is an MVC model (Model: Info in the DB, View: What can be seen, Controller: How developer Connects Model and View)
   
   this is why we have some files in the blog app, namely: model.py, views.py, urls.py
   
6. Then we create our Views and the Urls of our Views in the blog app, one more thing is to add these Urls also to the original project Urls file in jwitter

    To do this we need to import "path" and "include" from django.urls in the "urls.py" file of jwitter project

7. Now blog page and admin page are ready after running the server.

8. Any app in a Djamgo project needs to be installed first - we add our apps in the "jwitter/setting.py" file among other INSTALLED_APPS

   INSTALLED_APPS = [
    ...,
    'blog.apps.BlogConfig'
]



#### Create View, Model in blog app:
1. import HttpResponse

2. create a view/function which takes a request and always returns a HttpResponse

3. create the "urls.py" file in "blog" app folder to use it as a router for gathering the urls of the "blog" app

   to do this, import path from django.urls and import views.py file

4. Add the new path in the "jwitter/urls.py" file

5. Then we create a Model which is responsible for the auto-creation of a Database (using SQLite3); after saving the Model we will have a file called "db.sqlite3.sqlite3" in our "jwitter" project folder. It is SQLite3 because my default Database was that.

   the model is created for the Post's text

   class Post(models.Model): text = models.CharField(max_length=480)  # a class with one text field

6. After creating/changing a Model, we should also use this following code, to create the Model's migration file (makemigrations is a command to interact with Django Models). This file is "0001_initial.py".

  ... (venv)/jwitter> python manage.py makemigrations blog

8. Then we use "migrate" command to change the Database and apply all migrations

   This migration part is actually creating or applying the changes to the Database.

9. In order to create a superuser to be the admin and then be able to login:

   ... (venv)jwitter> python manage.py createsuperuser  # here we set the users info

10. NOW, run the server and login with the Admin's username and password; you can see the Admin's page.

11. Register the Post Model in admin.py file in the "blog" app by this code:

    from .models import Post
    admin.site.register(Post)

12. Now you can see that on the Admin page we have Post too and we can create a Post.

13. To show this on the site we should change our View, which was the index function previously. Change the index() to show all the posts that were created in our Post Model

    





