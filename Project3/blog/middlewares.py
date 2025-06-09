from django.shortcuts import HttpResponse, render

def my_func_middleware(get_response):
    print("One Time Initialization")

    def my_func(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    
    return my_func



# def my_func_middleware(get_response):
#     print("One Time Initialization")

#     def my_func(request):
#         print("This is before view")
#         # response = HttpResponse("Response from my_func Middleware")
#         response = render(request, 'blog/uc.html')
#         print("This is after view")
#         return response
    
#     return my_func


# Class based middleware
class MyClassMiddleware1:

    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time MyClassMiddleware1 Initialization")

    def __call__(self, request):
        print("This is MyClassMiddleware1 before view")
        response = self.get_response(request)
        print("This is MyClassMiddleware1 after view")
        return response


class MyClassMiddleware2:

    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time MyClassMiddleware2 Initialization")

    def __call__(self, request):
        print("This is MyClassMiddleware2 before view")
        response = self.get_response(request)
        print("This is MyClassMiddleware2 after view")
        return response


class MyClassMiddleware3:

    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time MyClassMiddleware3 Initialization3")

    def __call__(self, request):
        print("This is MyClassMiddleware3 before view")
        response = self.get_response(request)
        print("This is MyClassMiddleware3 after view")
        return response


# class MyProcessMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(request, *args, **kwargs):
#         print("This is Process View - Before View")
#         # return HttpResponse("This is before view")
#         return None


# class MyExceptionMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_exception(self, request, exception):
#         print("Exception Occured")
#         msg = exception
#         class_name = exception.__class__.__name__
#         print(class_name)
#         print(msg)
#         return HttpResponse(msg)


# class MyTemplateResponseMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_template_response(self, request, response):
#         print("Process Template Response From Middleware")
#         response.context_data['name'] = 'Rishabh'
#         return response