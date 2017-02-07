from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Welcome to Django E-Commerce'
    }
    return render(request, 'index.html', context)
