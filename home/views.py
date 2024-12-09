from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home_page(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def account_signup(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.rendre())