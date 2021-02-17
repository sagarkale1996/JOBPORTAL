from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50)
    esal= models.IntegerField()
    eexp = models.FloatField()


    def __str__(self):
        return f'{self.ename}'

class Employees(models.Model):

    ename = models.CharField(max_length=10)
    eaddress = models.CharField(max_length=30)
    eemail = models.CharField(max_length=20)
    ephone = models.IntegerField()
    def __str__(self):
        return f'{self.ename}'


def angel():
    pass

def vinay():
    pass





