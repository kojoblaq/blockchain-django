from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
import json


# Create your views here.
def home(request):
    if request.method =="GET":
        template = "fair_home.html"
        context={}
        # get all institutions
        all_institutions = Institution.objects.all()
        context['Inst'] = all_institutions
        # get all roles
        all_role = JobRole.objects.all()
        context['available_j'] = all_role
        # get all grades
        all_grade = Grade.objects.all()
        context['gradeLevel'] = all_grade
        # get all staff
        all_staff = Staff.objects.all()
        context['workers'] = all_staff
        print(context)
        return render(request,template,context) 
    try:        
        institution_nameeee = request.POST['institution']
        aliasee = request.POST['alias']
    except Exception as e:
        messages.error(request, str(e)+" is required")
        print("error")
        return redirect("/fairwages/fair_home/")  
    if request.method == "POST":
        inst = Institution()
        inst.institution_name = institution_nameeee
        inst.aliase = aliasee
        inst.save()
        messages.success(request,"Institution Added Succesfully!")              
        return redirect("/fairwages/fair_home/" )
    else:
      return redirect("/fairwages/fair_home/") 
      
# adding a job role
def job(request):        
    if request.method == "GET":
        template = "fair_home.html"
        return render(request,template)  
    try:
      company_name = request.POST['institution']
      job_t = request.POST['role']
    except Exception as e:
      messages.error(request, str(e)+" is required")
      print("role error")
      return redirect("/fairwages/fair_home/")      
      # return render(request,'fair_home.html',context)
    if request.method == "POST":
        job = JobRole()
        job.inst_name = Institution.objects.get(institution_name=company_name)
        job.job_title = job_t
        job.save()        
        messages.success(request,"Job Role successsfully created!")
        return redirect("/fairwages/fair_home/") 
    else:
        return redirect("/fairwages/fair_home/") 
      
 #adding a staff 
def stafff(request):
    if request.method == "GET":
       template = "fair_home.html"
       return render(request,template)  
    try:
      f_name = request.POST['fullname']
      stafff_id = request.POST['staffid']
      inst_name = request.POST['staff_institution']
      rolee = request.POST['role']
      ss_grade = request.POST['grade']      
    except Exception as e:
      messages.error(request, str(e)+" is required")
      print("staff error")
      return redirect("/fairwages/fair_home/")  
    if request.method == "POST":
        st_aff = Staff()
        st_aff.fullname = f_name
        st_aff.staff_id = stafff_id
        st_aff.company_name = Institution.objects.get(institution_name=inst_name)
        st_aff.job_role = JobRole.objects.get(id=int(rolee))
        st_aff.grade_level = Grade.objects.get(ss_grade_level = ss_grade)
        st_aff.save()
        messages.success(request,"Staff Added succesfully!")
        return redirect("/fairwages/fair_home/")
    else:
        return redirect("/fairwages/fair_home/") 
    
def grade(request):
    if request.method == "GET":
       template = "fair_home.html"
       return render(request,template)  
    try:
      staf_id = request.POST['g_staff_id']
      company_name = request.POST['g_institution']
      role = request.POST['g_role']
      grade_level = request.POST['g_grade'] 
      wage = request.POST['salary']
      s_fname = request.POST['g_fullname']
      
    except Exception as e:
      messages.error(request, str(e)+" is required")
      print(str(e))
      return redirect("/fairwages/fair_home/")
  
    if request.method == "POST":
        name = Institution.objects.get(institution_name=company_name)
        job_t = JobRole.objects.get(job_title=role)
        ss_grade = Grade.objects.get(ss_grade_level = grade_level)
        staff_fname = Staff.objects.get(fullname=s_fname)
        id_staf = Staff.objects.get(staff_id = staf_id)
        salary = Grade.objects.get(amount = float(wage))
        try:
          exists = GradeStructure.objects.get(name=name,job_t=job_t,ss_grade=ss_grade,staff_fname=staff_fname,id_staf=id_staf,salary=salary)
        except:
          g_rade = GradeStructure()
          g_rade.name = Institution.objects.get(institution_name=company_name)
          g_rade.job_t = JobRole.objects.get(job_title=role)
          g_rade.ss_grade = Grade.objects.get(ss_grade_level = grade_level)
          g_rade.staff_fname = Staff.objects.get(fullname=s_fname)
          g_rade.id_staf = Staff.objects.get(staff_id = staf_id)
          g_rade.salary = Grade.objects.get(amount = float(wage))               
          g_rade.save()
          messages.success(request,"New grade structure added!")
        else:
          messages.error(request,"This grade structure exists")
        return redirect("/fairwages/fair_home/") 
    else:
        return redirect("/fairwages/fair_home/")
      
      
def load_roles(request):
    template  = "fair_home.html"
    name_company = request.GET.get('staff_institution')
    inst = Institution.objects.get(institution_name=name_company)
    roles = JobRole.objects.filter(inst_name=inst).order_by('job_title')
    response_data = {}
    response_data['roles'] = [{'id':i.id,'job_title':i.job_title} for i in roles]
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    # return HttpResponse(request, template, {'rolee': roles}) 
    
def load_staff_byID(request):
  staff_id = request.GET.get('staff_id')
  staff = Staff.objects.get(staff_id=staff_id)
  response_data = {}
  response_data['staff'] = {'id':staff.id,'staff_id':staff.staff_id,'job_role':staff.job_role.job_title,'grade_level':staff.grade_level.ss_grade_level,'salary':staff.grade_level.amount,'company_name':staff.company_name.institution_name,'full_name':staff.fullname}
  return HttpResponse(json.dumps(response_data), content_type="application/json")