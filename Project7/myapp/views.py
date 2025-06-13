from django.shortcuts import render, HttpResponse
from myapp.forms import ContactForm

def myfunview1(request):
    return HttpResponse("Hello Function based View")

def myfunview2(request):
    return HttpResponse("<h1>Function based View</h1>")

def homefunview(request):
    return render(request, 'myapp/home.html')

def aboutfunview(request):
    context = {'msg': 'Welcome to GeekyShows Function Based View'}
    return render(request, 'myapp/about.html', context)


# def newsfunview(request):
#     template_name = 'myapp/news.html'
#     context = {'info': 'Subscribe to GeekyShows YT Channel'}
#     return render(request, template_name, context)

def newsfunview(request, template_name):
    template_name = template_name
    context = {'info': 'Subscribe to GeekyShows YT Channel'}
    return render(request, template_name, context)

def contactfunview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})
