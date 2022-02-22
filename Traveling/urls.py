"""Traveling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#this file to navigate routes for different applications in the same project
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('travel/', include('home.urls')),  #travel is root url  
                                            #this means any url for the travel then go to the url file for home app
                                            #whenever there's a url whis 127.0.01/travel -as root-, go to the home apllication and search for the url file => url.py
                                            #include function ensure it's another application in the same project
]
