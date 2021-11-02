from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Grade)
admin.site.register(Institution)
admin.site.register(JobRole)
admin.site.register(Staff)
admin.site.register(GradeStructure)


    
