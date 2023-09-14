from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # path("attraction", views.add_attraction, name= "add_attraction"),
    path("sun_set", views.sun_set, name= "sun_set"),
    
]