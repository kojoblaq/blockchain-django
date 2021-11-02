from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class useraccount(AbstractUser):
    # username = models.CharField(max_length=100, null = False)
    
    is_FW = models.BooleanField(default=False)
    is_MF = models.BooleanField(default=False)
    is_CaAG = models.BooleanField(default=False)
    
def __str__(self):
    return self.username
    