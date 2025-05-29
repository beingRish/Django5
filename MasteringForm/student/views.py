from django.shortcuts import render
from student.forms import ProfileForm
from student.models import Profile

def home(request):
    form = ProfileForm()
    return render(request, 'student/home.html', {'form': form})
