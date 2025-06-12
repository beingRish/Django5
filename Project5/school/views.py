from django.shortcuts import render
from school.models import Student


def home(request):
    student_data = Student.objects.all()
    # student_data = Student.objects.get_stu_roll_range(101, 105)

    context = {
        'students': student_data,
    }
    
    print("Return: ", student_data)
    return render(request, 'school/home.html', context)