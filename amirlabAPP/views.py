from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'home.html', {'page': 'home'})


def register(request):

    return render(request, 'register.html', {'page': 'register'})


def login(request):
    return render(request, 'login.html', {'page': 'login'})


def feeds(request):
    return render(request, 'feeds.html', {'page': 'feed'})



