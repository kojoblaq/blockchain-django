from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.

def home(request):
    template = "basetemp.html"
    
    return render(request,template)
