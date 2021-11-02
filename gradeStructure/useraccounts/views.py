from django.shortcuts import render, redirect
from .models import useraccount
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages



def signin(request):
   if request.method == "GET":
      template = "signin.html"
      return render(request,template)  
   try:
      username = request.POST['username']
      password = request.POST['password']
   except Exception as e:
      messages.error(request, str(e)+" is required")
      print("mother")
      return redirect("/useraccounts/signin/")

   auth = authenticate(request, username=username, password=password)
   if auth is not None:
      login(request, auth)
      messages.success(request, "Login successfully")
      print("login succesfully")
      
      if request.user.is_FW:
         return redirect("/fairwages/fair_home/")

      if request.user.is_MF:
         return redirect("/ministry/ministry_home/")

      if request.user.is_CaAG:
         return redirect("/controller/controller_home/")
      
   else:
      messages.error(request, "Please check your credentials")
      print("sister")
      return redirect("/useraccounts/signin/")  
   
   
     
   return redirect("/useraccounts/signin/")