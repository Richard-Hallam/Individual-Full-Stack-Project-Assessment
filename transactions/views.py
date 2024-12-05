from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def transactions_list(request):
    template = loader.get_template('transaction_list.html')
    return HttpResponse(template.render())