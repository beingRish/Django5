from django.shortcuts import render

def course(request):
    return render(request, 'cache/course.html')
