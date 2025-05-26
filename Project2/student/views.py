from django.shortcuts import render
from student.models import Profile
from student.forms import Registration, Login, Address

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

def registration(req):
    # form = Registration()
    form = Registration(field_order=['email', 'city'])
    return render(req,  'student/registration.html', {'form': form})

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
