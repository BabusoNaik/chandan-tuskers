from django.db import models

# Create your models here.

size_choices = (
      ('small','S'),
      ('medium','M'),
      ('large','L'),
      ('Ex-large','XL')

)


class User(models.Model):
    Name=models.CharField(max_length=128)
    Jersey_Name=models.CharField(max_length=128)
    jersey_Size=models.CharField(max_length=128,choices=size_choices,default='small')
    # email=models.EmailField(max_length=264,unique=True)
    jersey_Num=models.IntegerField(blank=True, null=True)
