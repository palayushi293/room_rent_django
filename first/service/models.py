from django.db import models
from tinymce.models import HTMLField




class Service(models.Model):
    service_title=models.CharField(max_length=60)
    service_description=models.CharField(max_length=180)
# Create your models here.


class Term(models.Model):
    service_title=models.CharField(max_length=200)
    service_des=HTMLField()


class Rent(models.Model):
    adress=models.CharField(max_length=100)
    bhk=models.CharField(max_length=3)    
    description=models.CharField(max_length=50)



# suppose if you want to provide editor html for description so that tage are ther and full editor mode is there then 
# from tinymce.models import HTMLField

## service+Desc=HTMLField()#