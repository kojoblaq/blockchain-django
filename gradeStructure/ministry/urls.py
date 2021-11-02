from django.conf.urls import url,include
from ministry import views
from django.urls import path
from django.contrib.auth.views import LogoutView



urlpatterns = [
# url(r"^useraccounts/signup/$",views.signup, name="signup"),
#url(r"^useraccounts/signin/$",views.signin, name="signin"),

# path('',views.home, name="home"),
url(r"^ministry/ministry_home/$",views.home, name="home"),



]