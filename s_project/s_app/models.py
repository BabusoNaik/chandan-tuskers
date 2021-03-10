from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=128)
    me=models.CharField(max_length=128,blank=True)
    Jersey_Name=models.CharField(max_length=128)
    # email=models.EmailField(max_length=264,unique=True)
    jersey_Num=models.IntegerField(blank=True, null=True)
    jersey_Nm=models.IntegerField(blank=True, null=True)
