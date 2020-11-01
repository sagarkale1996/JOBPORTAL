from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def Add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['Sid']
            name = form.cleaned_data['Sname']
            addr = form.cleaned_data['Saddr']
            schl = form.cleaned_data['Sscholarship']
            stu = Student(Sid=id,Sname=name,Saddr=addr,Sscholarship=schl)
            stu.save()
            return redirect('/Stu/Sview/')

    elif request.method == 'GET':
        stu = StudentForm()
        return render(request,template_name ='StudentApp/Stu_add.html',context={'stu':stu})

def View_stu(request):
    stu = Student.objects.all()
    return render(request,template_name='StudentApp/Sview.html',context={'stu':stu})

def Delete_student(request,id) :
    stu = Student.objects.get(id=id)
    stu.delete()
    return redirect('/Stu/Sview/')

def Update_Student(request,id):
    stu = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            stu.Sid = form.cleaned_data['Sid']
            stu.Sname = form.cleaned_data['Sname']
            stu.Saddr = form.cleaned_data['Saddr']
            stu.Sscholarship = form.cleaned_data['Sscholarship']
            stu.save()

            return redirect("SView")
        return redirect(request,'StudentApp/Update.html',{'stu':stu})

    elif request.method == 'GET':
        stu = StudentForm(initial={'Sid':stu.Sid,'Sname':stu.Sname,'Saddr':stu.Saddr,'Sscholarship':stu.Sscholarship})
        template_name = "StudentApp/Update.html"
        context = {'stu': stu}
        return render(request, template_name, context)




