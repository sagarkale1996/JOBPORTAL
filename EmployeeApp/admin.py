from django.contrib import admin
from .models import Employee,Employees


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','ename', 'esal', 'eexp']


admin.site.register(Employee,EmployeeAdmin)

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['ename','eaddress','eemail','ephone']

admin.site.register(Employees,EmployeesAdmin)
