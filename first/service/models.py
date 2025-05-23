from django.db import models
from tinymce.models import HTMLField
#from autoslug import AutoSlugField



class Service(models.Model):
    service_title=models.CharField(max_length=60)
    service_description=models.CharField(max_length=180)



class Term(models.Model):
    service_title=models.CharField(max_length=200)
    service_des=HTMLField()


class Rent(models.Model):
    adress=models.CharField(max_length=100)
    bhk=models.CharField(max_length=3)    
    description=models.CharField(max_length=50)
    

   # autoslug=AutoSlugField(populate_from ='adress', unique=True, null=True)
    def __str__(self):
        return f"{self.adress} - {self.bhk} BHK"


class booking(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    idproof=models.CharField(max_length=12)
    move_Date=models.DateTimeField()



# suppose if you want to provide editor html for description so that tage are ther and full editor mode is there then 
# from tinymce.models import HTMLField

## service+Desc=HTMLField()#