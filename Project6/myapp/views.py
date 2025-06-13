from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import httpx
import time
import asyncio
from asgiref.sync import sync_to_async, async_to_sync
from myapp.models import Student

async def home(request):
    async for student in Student.objects.all():
        print(f"name: {student.name} age: {student.age} email: {student.email}")

    # await Student.objects.acreate(
    #     name='kunal',
    #     age=30,
    #     email='kunal@example.com'
    # )

    # total_student = await Student.objects.acount()
    # print(total_student)

    # student = await Student.objects.aget(pk=1)
    # print(f"name: {student.name} age: {student.age} email: {student.email}")

    # student = await Student.objects.aget(pk=4)
    # await student.adelete()


    return render(request, 'myapp/home.html')


def product(request):
    return render(request, 'myapp/product.html')


def contact(request):
    return render(request, 'myapp/contact.html')


#Synchronous View
def sync_view(request):
    print("Inside Sync view")
    start_time = time.time()
    responses = []
    for _ in range(5):
        response = httpx.get("https://jsonplaceholder.typicode.com/posts")
        responses.append(response.json())

    end_time = time.time()
    time_taken = end_time - start_time
    return JsonResponse({
        'status': 'Success',
        'total_request': 5,
        'time_taken': f"{time_taken:.2f} seconds"
    })


#Asynchronous View
async def async_view(request):
    print("Inside Async view")
    start_time = time.time()

    async with httpx.AsyncClient() as client:
        tasks = [client.get("https://jsonplaceholder.typicode.com/posts") for _ in range(5)]
        responses = await asyncio.gather(*tasks)

    
    end_time = time.time()
    time_taken = end_time - start_time
    return JsonResponse({
        'status': 'Success',
        'total_request': 5,
        'time_taken': f"{time_taken:.2f} seconds"
    })


# Synchronous to Asynchronous

# Synchronous function
def my_sync_function1(x):
    return x * 2

# Asynchronous function
async def my_async_function1():
    result = await sync_to_async(my_sync_function1)(5)
    print(result)



# Asynchronous to Synchronous

# Asynchronous function
async def my_async_function2(x):
    return x * 2

def my_sync_function():
    result = async_to_sync(my_async_function2)(5)
    print(result)

# # heper method
# def get_student_data():
#     return list(Student.objects.filter(age=20).values())

# # view
# async def student_data(request):
#     student_data = await sync_to_async(get_student_data)()
#     return JsonResponse({'data': student_data})


# # Direct view without helper method
async def student_data(request):
    student_data = await sync_to_async(lambda: list(Student.objects.filter(age=20).values()))()
    return JsonResponse({'data': student_data})