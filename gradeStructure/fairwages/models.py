from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from gradeStructure.settings import AUTH_USER_MODEL


# Create your models here.

class Institution(models.Model):
    institution_name = models.CharField(max_length=500, null= False)
    aliase = models.CharField(max_length=10)
    def __str__(self):
        return self.institution_name
    
    
    
class JobRole(models.Model):
    inst_name = models.ForeignKey(Institution, on_delete=CASCADE, related_name="job")
    job_title = models.CharField(max_length=100, null= False)
    def __str__(self):
        return self.job_title

    
# class staff_grade(models.Model):
#     staff_name = models.CharField(max_length=1000, null = False)
#     job_title = models.ForeignKey(
#         JobRole, on_delete=models.CASCADE)
#     inst_name = models.ForeignKey(
#         Institution, on_delete=models.CASCADE)

   
    
class Grade (models.Model):
    GRADE_CHOICES = [('1H','1(H)'),('1L','1(L)'),                     
                     ('2H','2(H)'),('2L','2(L)'),                     
                     ('3H','3(H)'),('3L','3(L)'),                     
                     ('4H','4(H)'),('4L','4(L)'),                     
                     ('5H','5(H)'),('5L','5(L)'),                     
                     ('6H','6(H)'),('6L','6(L)'),                     
                     ('7H','7(H)'),('7L','7(L)'),                     
                     ('8H','8(H)'),('8L','8(L)'),                     
                     ('9H','9(H)'),('9L','9(L)'),                     
                     ('10H','10(H)'),('10L','10(L)'),                     
                     ('11H','11(H)'),('11L','11(L)'),                     
                     ('12H','12(H)'),('12L','12(L)'),                     
                     ('13H','13(H)'),('13L','13(L)'),                     
                     ('14H','14(H)'),('14L','14(L)'),                     
                     ('15H','15(H)'),('15L','15(L)'),                     
                     ('16H','16(H)'),('16L','16(L)'),                     
                     ('17H','17(H)'),('17L','17(L)'),                     
                     ('18H','18(H)'),('18L','18(L)'),                     
                     ('19H','19(H)'),('19L','19(L)'),                     
                     ('20H','20(H)'),('20L','20(L)'),                     
                     ('21H','21(H)'),('21L','21(L)'),                     
                     ('22H','22(H)'),('22L','22(L)'),                     
                     ('23H','23(H)'),('23L','23(L)'),                     
                     ('24H','24(H)'),('24L','24(L)'),                     
                     ('25H','25(H)'),('25L','24(L)'),                 
                     ]
    ss_grade_level = models.CharField(max_length=3, choices=GRADE_CHOICES, null= False)
    amount = models.FloatField(null = False)
    def __str__(self):
        return self.ss_grade_level
    
class Staff(models.Model):
    fullname = models.CharField(max_length=1000, null= False)
    staff_id = models.IntegerField(null=False, blank=False)
    job_role = models.ForeignKey(JobRole, on_delete=CASCADE, related_name = "role")
    grade_level = models.ForeignKey(Grade, on_delete=CASCADE, related_name="s_grade_level")
    company_name = models.ForeignKey(Institution, on_delete=CASCADE, related_name = "company_n")
    
    def __str__(self):
        return self.fullname
    # def __str__(me):
    #     return me.fullname



    
class GradeStructure (models.Model):
    GSTATUS = [
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Declined','Declined'),
    ]
    grade_id = models.AutoField(primary_key=True, null=False)
    name = models.ForeignKey(Institution, on_delete=CASCADE, related_name="name_of_inst")
    job_t = models.ForeignKey(JobRole, on_delete=CASCADE, related_name="title")
    ss_grade = models.ForeignKey(Grade,on_delete=CASCADE, related_name="g_level")
    id_staf = models.ForeignKey(Staff, on_delete=CASCADE, related_name="identity")
    staff_fname = models.ForeignKey(Staff, on_delete=CASCADE, related_name="fname")
    stat = models.CharField(max_length=200, null=True, blank=True, choices=GSTATUS, default='Pending')
    submission_date = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=CASCADE) 
    # creator = models.ForeignKey(AUTH_USER_MODEL,on_delete=CASCADE,default=1)
    who = models.CharField(max_length=50, null = False, blank= False)
    salary = models.ForeignKey(Grade, on_delete=CASCADE, related_name="wage")
    def __str__(self):
        return self.stat
    
