from django.shortcuts import render
from school.models import Student, Teacher
from django.db.models import Avg, Sum, Min, Max, Count
from datetime import date, time

# # This home view is for 'Working with Database Returns New Queryset'
# def home(request):
#     # student_data = Student.objects.all()

#     # student_data = Student.objects.filter(city='Gaya')      # Filter data which match
    
#     # student_data = Student.objects.exclude(city='Gaya')     # Filter data which doesn't match
    
#     # student_data = Student.objects.order_by('marks')     # Order by any column  -> Descending
#     # student_data = Student.objects.order_by('-marks')     # Order by any column -> Ascending
#     # student_data = Student.objects.order_by('name')     # Order by any column -> Name
#     # student_data = Student.objects.order_by('?')     # Order by any column -> Randomly
#     # student_data = Student.objects.order_by('name').reverse()     # Order by any column -> name(reversed)
#     # student_data = Student.objects.order_by('name')[0:5]     # Order by any column -> name(5)

#     # student_data = Student.objects.values()   # returns all the values in dictionary forms
#     # student_data = Student.objects.values('id', 'city')   # returns specific id and city columns value in dictionary forms
#     # student_data = Student.objects.values_list()    # returns all the values in tupple forms
#     # student_data = Student.objects.values_list('id', 'name')    # returns specific id and name columns value in tupple forms
#     # student_data = Student.objects.values_list('id', 'name', named=True)    # returns specific id and name columns value in tupple forms with named tupple

#     # qs1 = Student.objects.values_list('id', 'name', named=True)
#     # qs2 = Teacher.objects.values_list('id', 'name', named=True)
#     # student_data = qs2.union(qs1)

#     # qs1 = Student.objects.values_list('id', 'name', named=True)
#     # qs2 = Teacher.objects.values_list('id', 'name', named=True)
#     # student_data = qs2.union(qs1, all=True)

#     # qs1 = Student.objects.values_list('id', 'name', named=True)
#     # qs2 = Teacher.objects.values_list('id', 'name', named=True)
#     # student_data = qs2.intersection(qs1)

#     # qs1 = Student.objects.values_list('id', 'name', named=True)
#     # qs2 = Teacher.objects.values_list('id', 'name', named=True)
#     # student_data = qs1.difference(qs2)

#     # student_data = Student.objects.filter(name="Vishwjeet") & Student.objects.filter(city="Banglore")
#     # student_data = Student.objects.filter(name="Vishwjeet", city="Banglore")
    

#     student_data = Student.objects.filter(name="Vishwjeet") | Student.objects.filter(city="Gaya")
    
#     print("All Data: ", student_data)
#     # print()
#     # print("SQL Query: ", student_data.query)
#     return render(request, 'school/home.html', {'students': student_data})








# # This home view is for 'Working with Database Not Returns Queryset
# def home(request):
#     student_data = Student.objects.get(pk=2)
#     # student_data = Student.objects.first()
#     # student_data = Student.objects.order_by('name').first()

#     # student_data = Student.objects.last()
#     # student_data = Student.objects.order_by('name').last()

#     # student_data = Student.objects.latest('pass_date')
#     # student_data = Student.objects.latest('pass_date', 'id')

#     # student_data = Student.objects.earliest('pass_date')
#     # student_data = Student.objects.all()
#     # # print(student_data.exists())
#     # one_data = Student.objects.get(pk=2)
#     # print(student_data.filter(pk=one_data.pk).exists())


#     # student_data = Student.objects.create(name='Sameer', roll=114, city='Bokaro', marks=60, pass_date='2020-5-4')


#     # student_data, created = Student.objects.get_or_create(name='Anisa', roll=115, city='Bokaro', marks=60, pass_date='2020-5-4')
#     # print(created)

#     # student_data = Student.objects.filter(id=12).update(name='Kabir', marks=80)

#     # student_data = Student.objects.filter(marks=100).update(city='Delhi')


#     # student_data, created = Student.objects.update_or_create(id=13, name='Anisa', defaults={'name': 'Kohli', 'roll': 156})

#     # student_data, created = Student.objects.update_or_create(id=14, name='Kohli', defaults={'name': 'Dhoni', 'roll': 157, 'marks': 200, 'pass_date': '2020-5-4'})



#     #                   # Bulk Create
#     # objs = [
#     #     Student(name='Atif', roll=116, city='Dhanbad', marks=70, pass_date='2020-5-4'),
#     #     Student(name='Sahil', roll=117, city='Bokaro', marks=50, pass_date='2020-5-6'),
#     #     Student(name='Kumar', roll=118, city='Dhanbad', marks=30, pass_date='2020-5-9'),
#     # ]

#     # student_data = Student.objects.bulk_create(objs)


#     #                 # Bulk Update
#     # all_student_data = Student.objects.all()
#     # for stu in all_student_data:
#     #     stu.city = 'Mumbai'
#     # student_data = Student.objects.bulk_update(all_student_data, ['city'])


#     #                     # In Bulk
#     # student_data = Student.objects.in_bulk([1, 3])
#     # print(student_data[3].name)
#     # student_data = Student.objects.in_bulk([])
#     # student_data = Student.objects.in_bulk()



#                         # Delete
#     # student_data = Student.objects.get(pk=11).delete()
#     # student_data = Student.objects.filter(marks=70).delete()
#     # student_data = Student.objects.all().delete()   # Carefully! it will delete all data


#                         # Count
#     print(Student.objects.all().count())


#     print("Return: ", student_data)
#     return render(request, 'school/home.html', {'student': student_data})








# # This home view is for 'Working with Database Field Lookups
# def home(request):
#     # student_data = Student.objects.all()
#     # student_data = Student.objects.filter(name__exact='Sonam')  # case sensitive
#     # student_data = Student.objects.filter(name__iexact='Sonam')  #case ensensitive
#     # student_data = Student.objects.filter(name__contains='S')  # case sensitive -> might not work with sqlite but work with mySQL, and PostgreSQL
#     # student_data = Student.objects.filter(name__icontains='i')  # case ensensitive
#     # student_data = Student.objects.filter(id__in=[1, 3, 7])
#     # student_data = Student.objects.filter(marks__gt=200)
#     # student_data = Student.objects.filter(marks__gte=200)
#     # student_data = Student.objects.filter(marks__lt=200)
#     # student_data = Student.objects.filter(name__startswith='S')
#     # student_data = Student.objects.filter(name__istartswith='S')
#     # student_data = Student.objects.filter(name__endswith='t')
#     # student_data = Student.objects.filter(name__iendswith='t')
#     # student_data = Student.objects.filter(pass_date__range=('2024-01-01', '2024-12-24'))
#     # student_data = Student.objects.filter(pass_date__range=('2024-01-01', '2024-12-24'))
#     # student_data = Student.objects.filter(admission_date__date=date(2023, 8, 15))
#     # student_data = Student.objects.filter(admission_date__date__gt=date(2023, 8, 15))
#     # student_data = Student.objects.filter(admission_date__date__lt=date(2023, 8, 15))
#     # student_data = Student.objects.filter(pass_date__year=2023)
#     # student_data = Student.objects.filter(pass_date__year__gt=2023)
#     # student_data = Student.objects.filter(pass_date__year__lt=2023)
#     # student_data = Student.objects.filter(pass_date__month=12)
#     # student_data = Student.objects.filter(pass_date__month__gt=5)
#     # student_data = Student.objects.filter(pass_date__month__lt=5)
#     # student_data = Student.objects.filter(pass_date__day=4)
#     # student_data = Student.objects.filter(pass_date__day__gt=4)
#     # student_data = Student.objects.filter(pass_date__day__lt=4)
#     # student_data = Student.objects.filter(pass_date__week=15)
#     # student_data = Student.objects.filter(pass_date__week__gt=15)
#     # student_data = Student.objects.filter(pass_date__week__lt=15)
#     # student_data = Student.objects.filter(pass_date__week_day=4)
#     # student_data = Student.objects.filter(pass_date__week_day__gt=4)
#     # student_data = Student.objects.filter(pass_date__week_day__lt=4)
#     # student_data = Student.objects.filter(pass_date__quarter=1)
#     # student_data = Student.objects.filter(pass_date__quarter__gt=2)
#     # student_data = Student.objects.filter(pass_date__quarter__lt=2)
#     # student_data = Student.objects.filter(admission_date__time=time(6,00))
#     # student_data = Student.objects.filter(admission_date__time__gt=time(10,00))
#     # student_data = Student.objects.filter(admission_date__time__lt=time(10,00))
#     # student_data = Student.objects.filter(admission_date__hour=6)
#     # student_data = Student.objects.filter(admission_date__hour__gt=10)
#     # student_data = Student.objects.filter(admission_date__hour__lt=10)
#     # student_data = Student.objects.filter(admission_date__minute=57)
#     # student_data = Student.objects.filter(admission_date__minute__gt=40)
#     # student_data = Student.objects.filter(admission_date__minute__lt=40)
#     # student_data = Student.objects.filter(admission_date__second=57)
#     # student_data = Student.objects.filter(admission_date__second__gt=40)
#     # student_data = Student.objects.filter(admission_date__second__lt=40)
#     student_data = Student.objects.filter(roll__isnull=False)
    

#     print("Return: ", student_data)
#     return render(request, 'school/home.html', {'students': student_data})








# This home view is for 'Working with Database Aggregate Function'
def home(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    total = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    totalCount = student_data.aggregate(Count('marks'))





    context = {
        'students': student_data,
        'average': average,
        'total': total,
        'minimum': minimum,
        'maximum': maximum,
        'totalCount': totalCount,
    }
    
    print("Return: ", student_data)
    return render(request, 'school/home.html', context)