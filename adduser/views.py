from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def index(request):
    return HttpResponse("<h1>this is the music app homepage</h1>")
