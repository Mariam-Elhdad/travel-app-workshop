from cgitb import html
from django.urls import URLPattern, path
from . import views


urlpatterns =[ 
    path('', views.Home, name= 'home-page'),
    path('/profile', views.Profile, name= 'profile-page'),
    path('/registration', views.Registration, name= 'registration-page'),

]

