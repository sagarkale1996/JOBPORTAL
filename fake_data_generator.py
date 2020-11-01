import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","JOBPORTAL.settings")

import django
django.setup()

import random
from faker import Faker
fake = Faker()

from EmployeeApp.models import Employees

def Employeess(rows):
    for i in range(rows):
        n = fake.name()
        a = fake.address()
        e = fake.email()
        p = random.randint(1111111111,9999999999)
        obj = Employees(ename=n,eaddress=a,eemail=e,ephone=p)
        obj.save()
        print("fake employees are generated")

Employeess(1)
print('email',fake.email())
print('name',fake.name())
print('phoneno',fake.lname())








