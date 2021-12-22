from fairwages.models import GradeStructure
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import LANGUAGE_SESSION_KEY
from useraccounts.models import useraccount
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required
import requests as r


# Create your views here.

def home(request):
    template = "basetemp.html"
    context={}
    pendingcases = GradeStructure.objects.filter(stat="Pending")
    context["allpending"] = pendingcases
    approvedcases = GradeStructure.objects.filter(stat="Approved")
    context["allapproved"] = approvedcases
    allgrades = GradeStructure.objects.all()
    context["allgrades"] = allgrades 
    
    return render(request,template,context)

# def api_call(request):
#     url = "http://localhost:3000/get-grades"
#     # params = {"staff_id":staff_id}
#     try:  
#         resp = r.get(url)
#     except Exception as e:  
#         print(str(e))
#     print(resp.text)
    
#     return JsonResponse(resp.json())
    
# def grades_grade(request):
#     qs = GradeStructure.objects.all()
#     data = serialize("json", qs, 
#                      fields=('grade_id', 
#                              'name','job_t',
#                              'ss_grade',
#                              'id_staf',
#                              'staff_fname',
#                              'stat',
#                              'submission_date',
#                              'salary'))
#     return HttpResponse(data, content_type="application/json")




@login_required(login_url='signin')
def pendinggrades(request):
    template = "basetemp.html"
    context={}
    if request.user.is_MF:
        allpendingcases = GradeStructure.objects.filter(status="Pending")
        context["allpending"]= allpendingcases
        allgrades = GradeStructure.objects.all()
        context["allgrades"] = allgrades
    
        if request.method == "POST":
            actions = request.POST['actions']   
            print(actions)    
                 
            if actions == "Approve":                        
                #getting user who perfomed the action
                user = request.user.username
                #getting the id of post to approve
                g_id = request.POST["d_id"]  
                print(g_id)              
                approvedgrade =GradeStructure.objects.get(grade_id=g_id)
                approvedgrade.stat = "Approved"
                approvedgrade.save()    
                            
                return render(request,template,context)
            
            if actions == "Decline":
                #getting user who perfomed the action
                # user = request.user.username
                #getting the id of post to approve
                g_id = request.POST["d_id"]
                declinegrade =GradeStructure.objects.get(grade_id=g_id)
                declinegrade.stat = "Decline"
                declinegrade.save()                
                return render(request,template,context)          
            
    else:
        return render(request,template)      
    return render(request,template,context)



@login_required(login_url='signin')
def approvedgrades(request):
    template = "approved.html"
    context={}
    if request.user.is_MF:
        allpendingcases = GradeStructure.objects.filter(status="Approved")
        context["allapproved"]= allpendingcases
    return render(request,template,context)
