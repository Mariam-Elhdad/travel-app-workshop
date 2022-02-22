from django.urls import URLPattern, path
from . import views

urlpatterns = [ 
    path('', views.Home, name='home'),# the empty string means that it's the main route, and other routes will displayed after the (/home/)
    # path('about/',views.home, name= 'about')
    # path('/profile', views.Profile, name= 'profile-page'),
    # path('/registration', views.Registration, name= 'registration-page'),

]

