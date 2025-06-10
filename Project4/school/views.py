from django.shortcuts import render
from school.models import Student, Teacher
from django.db.models import Q

# Create your views here.
def home(request):
    # all_data = Student.objects.all()

    # all_data = Student.objects.filter(city='Gaya')      # Filter data which match
    
    # all_data = Student.objects.exclude(city='Gaya')     # Filter data which doesn't match
    
    # all_data = Student.objects.order_by('marks')     # Order by any column  -> Descending
    # all_data = Student.objects.order_by('-marks')     # Order by any column -> Ascending
    # all_data = Student.objects.order_by('name')     # Order by any column -> Name
    # all_data = Student.objects.order_by('?')     # Order by any column -> Randomly
    # all_data = Student.objects.order_by('name').reverse()     # Order by any column -> name(reversed)
    # all_data = Student.objects.order_by('name')[0:5]     # Order by any column -> name(5)

    # all_data = Student.objects.values()   # returns all the values in dictionary forms
    # all_data = Student.objects.values('id', 'city')   # returns specific id and city columns value in dictionary forms
    # all_data = Student.objects.values_list()    # returns all the values in tupple forms
    # all_data = Student.objects.values_list('id', 'name')    # returns specific id and name columns value in tupple forms
    # all_data = Student.objects.values_list('id', 'name', named=True)    # returns specific id and name columns value in tupple forms with named tupple

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # all_data = qs2.union(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # all_data = qs2.union(qs1, all=True)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # all_data = qs2.intersection(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # all_data = qs1.difference(qs2)

    # all_data = Student.objects.filter(name="Vishwjeet") & Student.objects.filter(city="Banglore")
    # all_data = Student.objects.filter(name="Vishwjeet", city="Banglore")
    

    all_data = Student.objects.filter(name="Vishwjeet") | Student.objects.filter(city="Gaya")
    
    print("All Data: ", all_data)
    # print()
    # print("SQL Query: ", all_data.query)
    return render(request, 'school/home.html', {'all_data': all_data})