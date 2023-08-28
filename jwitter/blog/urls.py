from django.urls import path
from . import views

urlpatterns = [
    # we made a view named index, so that if in the main urls file we did not say any special path, meaning ''
    # it will show this index view
    # now go to the main urls file which is in the jwitter and add this path you wrote
    # do this adding via include and import it too
    path('', views.index, name='index')
]