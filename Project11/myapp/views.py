from django.shortcuts import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View

def home_view(request):
    url = reverse('home')
    print(url)
    return HttpResponse("<h1>Home Page Function based view</h1>")


def product_view(request, pk):
    url = reverse('product', kwargs={'pk': pk})
    print(url)
    return HttpResponse("<h1>Product Page Function based view</h1>")


class AboutView(View):
    def get(self, request, *args, **kwargs):
        url = reverse_lazy('about')
        print(url)
        return HttpResponse("<h1>About Page Class based view</h1>")


class PostView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        url = reverse_lazy('post', kwargs={'pk': pk})
        print(url)
        return HttpResponse("<h1>Post Page Class based view</h1>")