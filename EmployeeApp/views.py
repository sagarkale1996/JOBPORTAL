from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def Home(request):
    template_name = "EmployeeApp/base.html"
    context = {}
    return render(request,template_name,context)
def About(request):
    template_name="EmployeeApp/about.html"
    context = {}
    return render(request, template_name, context)
@login_required()
def Add_Emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Emp/view/')
        return render(request,template_name='EmployeeApp/view_emp.html',context={'emp':form})

    elif request.method =='GET':
        emp = EmployeeForm()
        template_name= "EmployeeApp/add_emp.html"
        context = {'emp':emp}
        return render(request,template_name,context)

def View_Emp(request):
    emp = Employee.objects.all()
    template_name = "EmployeeApp/view_emp.html"
    context = {'emp':emp}
    return render(request,template_name="EmployeeApp/view_emp.html",context={'emp':emp})

def delete(request,id):
    emp = Employee.objects.get(eid=id)
    emp.delete()
    return redirect(View_Emp)

"""https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
"""

def Update_Emp(request,id):
    em = Employee.objects.get(eid=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=em)
        if form.is_valid():
            form.save()
            return redirect("/Emp/view/")
        return render(request,"EmployeeApp/update.html",{'em':em})
    else :
        emp = EmployeeForm(instance=em)
        template_name= "EmployeeApp/update.html"
        context = {'emp':emp}
        return render(request,template_name,context)

def loginView(request):
    if request.method == 'GET':
        template_name = 'EmployeeApp/login.html'
        context = {}
        return render(request, template_name, context)

    elif request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pw']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('view_emp')

        else:
            template_name = 'EmployeeApp/login.html'
            messages.error(request, '')
            context = {}
            return render(request, template_name, context)


def logoutView(request):
    logout(request)
    return redirect('login')




