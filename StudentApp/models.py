from django.db import models

# Create your models here.
class Student(models.Model):
    Sid = models.IntegerField()
    Sname = models.CharField(max_length=20)
    Saddr = models.CharField(max_length=50)
    Sscholarship = models.FloatField()
    Simg = models.ImageField(null=True,blank=True,upload_to='images')

