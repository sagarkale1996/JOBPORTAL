from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Company,Jobs
# Create your views here.
class Companylist(ListView):
    model = Company
    template_name = 'CompanyApp/base1.html'

    context_object_name = 'comp'

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'CompanyApp/comp_detail.html'

class CreateCompanyView(CreateView):
    model = Company
    fields = '__all__'
    success_url = '/Cmp/list/'

class UpdateCompanyView(UpdateView):
    model = Company
    fields = '__all__'
    success_url = '/Cmp/list/'

class DeleteCompanyView(DeleteView):
    model = Company
    success_url = '/Cmp/list/'



class Jobslist(ListView):
    model = Jobs
    context_object_name = 'Jbs'
    template_name = 'CompanyApp/jobs_list.html'

class CreateJobsView(CreateView):
    model = Jobs
    fields = '__all__'
    success_url = '/Cmp/Jlist/'


class JobsDetailView(DetailView):
    model = Jobs
    template_name = "CompanyApp/jobs_detail.html"


class JobsUpdateView(UpdateView):
    model = Jobs
    fields = '__all__'
    success_url = '/Cmp/Jlist/'

class JobsDeleteView(DeleteView):
    model = Jobs
    fields = '__all__'
    success_url = '/Cmp/Jlist/'


