from django.db import models
from datetime import datetime

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=50,default= 'hp')
    ram = models.PositiveSmallIntegerField(default = 4)

    
class Phone(models.Model):
    name = models.CharField(max_length=60,default = 'samsung a12')
    pub_date = models.DateTimeField(default =datetime.now)
    


