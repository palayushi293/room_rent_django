from django.db import models

class Service(models.Model):
    service_title=models.CharField(max_length=60)
    service_description=models.CharField(max_length=180)
# Create your models here.
