from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import useraccount

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = useraccount()
    fieldsets = UserAdmin.fieldsets + (
      ('Extra Fields', {'fields':
       ('is_FW',
       'is_MF','is_CaAG')}),
     )
admin.site.register(useraccount, CustomUserAdmin)
