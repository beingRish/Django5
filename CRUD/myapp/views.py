from django.shortcuts import render
from myapp.models import Student
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'roll']
    success_url = '/student/'

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'roll']
    success_url = '/student/'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/student/'
