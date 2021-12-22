from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class useraccount(AbstractUser): 
    is_FW = models.BooleanField(default=False)
    is_MF = models.BooleanField(default=False)
    is_CaAG = models.BooleanField(default=False)
def __str__(self):
    return self.username
    