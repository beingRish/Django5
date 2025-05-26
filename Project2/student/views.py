from django.shortcuts import render
from student.models import Profile
from student.forms import Registration, Login, Address, DemoForm
from django.http import HttpResponseRedirect

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
    if req.method == 'POST':
        form = Registration(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('name: ', name)
            print('email: ', email)
            print('password: ', password)
            return HttpResponseRedirect('/student/success')
    else:
        form = Registration()
    return render(req,  'student/registration.html', {'form': form})

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