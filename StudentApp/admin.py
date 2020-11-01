from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Sid','Sname','Saddr','Sscholarship']

admin.site.register(Student,StudentAdmin)
