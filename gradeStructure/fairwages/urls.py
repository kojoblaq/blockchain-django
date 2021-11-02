from django.conf.urls import url,include
from fairwages import views
from django.urls import path
from django.contrib.auth.views import LogoutView

import fairwages



urlpatterns = [
# url(r"^useraccounts/signup/$",views.signup, name="signup"),
#url(r"^useraccounts/signin/$",views.signin, name="signin"),

# path('',views.home, name="home"),
url(r"^fairwages/fair_home/$",views.home, name="home"),
url(r"^fairwages/job/$",views.job, name="job"),
url(r"^fairwages/staff/$",views.stafff, name = "staff"),
url(r"^fairwages/grade/$",views.grade, name = "grade"),
url(r"^ajax/load-roles/",views.load_roles, name = "ajax_load_roles"),
url(r"^ajax/load-staff/",views.load_staff_byID, name = "ajax_load_staff")
# url(r"^fairwages/structure/$",views.structure, name = "structure")




]   