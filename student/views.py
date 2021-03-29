from django.shortcuts import render,redirect
from .forms import StudentForms
from .models import Student
# Create your views here.

def StudentHome(request):
    return render(request,'student/home.html')

def StudentForm(request,id=0):
    if request.method=="GET":
        if id==0:
            form=StudentForms()
        else:
            student=Student.objects.get(pk=id)
            form=StudentForms(instance=student)
        return render(request,'student/student_form.html',{'form':form})
    else:
        if id==0:
            form=StudentForms(request.POST)
        else:
            student=Student.objects.get(pk=id)
            form=StudentForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
   

def StudentList(request):
    context={'student_lis':Student.objects.all()}
    return render(request,'student/student_list.html',context)

def StudentDelete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect("student_list")
