from django.shortcuts import render, HttpResponse
from myapp.forms import ContactForm
from django.views import View
from django.views.generic.base import TemplateView

def myfunview1(request):
    return HttpResponse("Hello Function Based View")

class MyClassView1(View):
    def get(self, request):
        return HttpResponse("Hello Class Based View")


def myfunview2(request):
    return HttpResponse("<h1>Function Based View</h1>")

class MyClassView2(View):
    def get(self, request):
        return HttpResponse("<h1>Class Based View</h1>")

class MyClassView3(View):
    name = 'Rishabh'
    def get(self, request):
        return HttpResponse(self.name)

class MyChildClassView3(MyClassView3):
    def get(self, request):
        return HttpResponse(self.name)


def homefunview(request):
    return render(request, 'myapp/home.html')

class HomeClassView(View):
    def get(self, request):
        return render(request, 'myapp/home.html')


def aboutfunview(request):
    context = {'msg': 'Welcome to GeekyShows Function Based View'}
    return render(request, 'myapp/about.html', context)

class AboutClassView(View):
    def get(self, request):
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

class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info': 'Subscribe to GeekyShows YT Channel'}
        return render(request, self.template_name, context)


def contactfunview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})

class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'myapp/contact.html', {'form': form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')
        

# TemplateView
class AboutTemplateView(TemplateView):
    template_name = 'myapp/about.html'

class ContactTemplateView(TemplateView):
    template_name = 'myapp/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Rishabh'
        context['roll'] = 101

        return context

class ProfileTemplateView(TemplateView):
    template_name = 'myapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Rishabh'
        print(context)
        print(kwargs)

        return context