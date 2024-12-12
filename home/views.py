from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def account_signup(request):
    return render(request, 'signup.html')