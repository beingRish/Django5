from django.shortcuts import render
from student.models import Profile
from student.forms import Login, Address, DemoForm
from django.http import HttpResponseRedirect
from student.models import User
from student.modelForm import StudentRegistration, TeacherRegistration
from django.contrib import messages

# Create your views here.
def all_data(req):
    all_students = Profile.objects.all()
    print(all_students)
    return render(req, 'student/all.html', {'students': all_students})

def single_data(req):
    # single_student = Profile.objects.get(pk=1)
    # single_student = Profile.objects.get(id=2)
    single_student = Profile.objects.get(name='Vishwjeet')
    print(single_student)
    return render(req, 'student/single.html', {'student': single_student})

def student_form_view(req):
    if req.method == 'POST':
        form = StudentRegistration(req.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            cpw = form.cleaned_data['confirm_password']
            # Save Data into Database
            # Syntax:- save(commit=False/True)
            user = User(name=nm, email=em, password=pw)
            user.save()
            # Update Data into Database
            # user = User(id=1, name=nm, email=em, password=pw)
            # user.save()
            # Delete Data from Database
            # user = User(id=2)
            # user.delete()
            messages.success(req, "Registeration Success !!!")
            # return HttpResponseRedirect('/student/student-register/')
    else:
        form = StudentRegistration()
    return render(req,  'student/student_registration.html', {'form': form})

def teacher_form_view(req):
    if req.method == 'POST':
        form = TeacherRegistration(req.POST)
        if form.is_valid():
            tnm = form.cleaned_data['teacher_name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            user = User(teacher_name=tnm, email=em, password=pw)
            user.save()
    else:
        form = TeacherRegistration()
    return render(req,  'student/teacher_registration.html', {'form': form})

def reg_success(req):
    return render(req, 'student/success.html')

def login(req):
    form = Login()

    # form = Login(auto_id='rishabh_%s')
    # form = Login(auto_id=True)
    # form = Login(auto_id=False)
    # form = Login(auto_id='Rishabh')

    # form = Login(label_suffix='A')
    # form = Login(label_suffix=' ')

    # form = Login(initial={'email': 'rishabh@example.com', 'password': 'rishabh12345'})

    return render(req,  'student/login.html', {'form': form})

def address(req):
    form = Address()
    return render(req,  'student/address.html', {'form': form})

def demo_form(req):
    form = DemoForm()
    return render(req, 'student/demoform.html', {'form': form})