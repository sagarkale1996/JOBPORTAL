from django.contrib import admin

# Register your models here.
from .models import Company,Jobs


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','loc','type','domain']

admin.site.register(Company,CompanyAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ['desg','ctc','exp','loc','skills']

admin.site.register(Jobs,JobAdmin)
