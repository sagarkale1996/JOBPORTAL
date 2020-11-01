from django.db import models

# Create your models here.

ch=     (('Service Based','Service Based'),
        ('Product based','Product Based'),
        ('Startup','Startup'))

class Company(models.Model):
    name = models.CharField(max_length=20)
    loc = models.CharField(max_length=20)
    type = models.CharField(max_length=20,choices=ch)
    domain = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Jobs(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    desg = models.CharField(max_length=20)
    ctc = models.FloatField()
    exp = models.FloatField()
    loc = models.CharField(max_length=20)
    skills = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.company}'

    #babya1 123

