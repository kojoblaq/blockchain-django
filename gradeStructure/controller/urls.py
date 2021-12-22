from django.conf.urls import url,include
from controller import views
from django.urls import path
from django.contrib.auth.views import LogoutView



urlpatterns = [
# url(r"^useraccounts/signup/$",views.signup, name="signup"),
#url(r"^useraccounts/signin/$",views.signin, name="signin"),

# path('',views.home, name="home"),
url(r"^controller/controller_home/$",views.home, name="home"),
url(r"^controller/pending/$",views.pendinggrades, name="pending")



]