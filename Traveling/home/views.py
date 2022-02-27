from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return(HttpResponse('<h1> Its home page </h1>'))
    

def Profile(request):
    return(HttpResponse('<h1> Its your profile page </h1>'))

def Registration(request):
    return(HttpResponse('<h1> Its your registration page </h1>'))   


print("hello worlds")