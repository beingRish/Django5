from django.shortcuts import render
from django.views.decorators.cache import cache_page

def home(request):
    return render(request, 'cache/home.html')


# @cache_page(30)
def course(request):
    return render(request, 'cache/course.html')


def result(request):
    return render(request, 'cache/result.html')
