from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle

def home(request):
    context = {
        'posts': Vehicle.objects.all()
    }
    return render(request, 'home/home.html', context)
    
def about(request):
    return render(request, 'home/about.html')


# def Profile(request):
#     return(HttpResponse('<h1> Its your profile page </h1>'))

# def Registration(request):
#     return(HttpResponse('<h1> Its your registration page </h1>'))   