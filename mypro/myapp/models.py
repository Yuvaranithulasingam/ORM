from django.db import models
from django.contrib import admin
class Stud (models.Model):
    name=models.CharField(max_length=100)
    registernumber=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    department=models.CharField(max_length=50)
    collegename=models.CharField(max_length=100)
class StudAdmin(admin.ModelAdmin):
    list_display=('name','registernumber','age','email','department','collegename')

from django.contrib import admin
from .models import Stud,StudAdmin
admin.site.register(Stud,StudAdmin)



# Create your models here.
