from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache

def home(request):
    return render(request, 'cache/home.html')


# @cache_page(30)
def course(request):
    return render(request, 'cache/course.html')


def result(request):
    return render(request, 'cache/result.html')


# def movie(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'Herry Poter', 60)
#         mv = cache.get('movie')

#     return render(request, 'cache/movie.html', {'mv': mv})


# def movie(request):
#     mv = cache.get_or_set('movie', 'Hello The Harry', 60)
#     mv1 = cache.get_or_set('movie', 'Hello The Harry', 60, version=2)
#     print('mv1:', mv1)
#     return render(request, 'cache/movie.html', {'mv': mv})


# def movie(request):
#     data = {'name': 'Ritik', 'roll': 101}
#     cache.set_many(data, 30)
#     stu = cache.get_many(data)
#     # return render(request, 'cache/movie.html', {'mv': mv})
#     return render(request, 'cache/movie.html', {'stu': stu})


# def movie(request):
#     cache.delete('movie', 2)
#     return render(request, 'cache/movie.html')


# def movie(request):
#     i = cache.incr('roll', delta=2)
#     print(i)
#     return render(request, 'cache/movie.html')


# def movie(request):
#     cache.clear() // Do not clear cache from the view, always do with terminal
#     return render(request, 'cache/movie.html')
