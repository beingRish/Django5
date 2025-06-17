from django.shortcuts import HttpResponse
from django.views import View
from django.http import JsonResponse
from myapp.models import Product
from django.core.serializers import serialize
import json

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("<h1>Home Page</h1>")

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'message': 'Home Page',
#             'status': 'success'
#         }
#         return JsonResponse(data)

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'message': 'Home Page',
#             'status': 'success'
#         }
#         return JsonResponse(data, status=201)

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         data = ['rishabh', 'ritik', 'vishwjeet', 'shashank']
#         return JsonResponse(data, safe=False)

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'message': 'Home Page',
#             'status': 'success'
#         }
#         response = JsonResponse(data)
#         response['X-custom-header'] = 'CustomValue'
#         return response

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         products = json.loads(serialize('json', Product.objects.all()))
#         return JsonResponse(products, safe=False)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        products = list(Product.objects.values('id', 'name', 'price'))
        return JsonResponse(products, safe=False)