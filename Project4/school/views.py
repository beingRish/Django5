from django.shortcuts import render
from school.models import Student, Teacher
from django.db.models import Q

# Create your views here.
def home(request):
    all_data = Student.objects.all()
    print("All Data:", all_data)

    return render(request, 'school/home.html', {'all_data': all_data})