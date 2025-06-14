from django.shortcuts import render
from django.views import View
from myapp.models import Student
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class AllStudentView(View):
    def get(self, request):
        all_students = Student.objects.all()
        return render(request, 'myapp/all_student.html', {'all_students': all_students})
    
class SingleStudentView(View):
    def get(self, request, pk):
        single_student = Student.objects.get(pk=pk)
        return render(request, 'myapp/single_student.html', {'single_student': single_student})
    

# List View

class StudentListView(ListView):
    model = Student
    
class StudentListView1(ListView):
    model = Student
    template_name_suffix = '_all'
    ordering=['name']
    
class StudentListView2(ListView):
    model = Student
    template_name = 'myapp/students.html'
    context_object_name = 'students'
    
class StudentListView3(ListView):
    model = Student
    template_name = 'myapp/sabhistudents.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course='Python')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['django_students'] = Student.objects.filter(course='Django')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES.get('user') == 'sonam':
            template_name = 'myapp/sonam.html'
        else:
            template_name = self.template_name
        return [template_name]
    

# Detail View

class StudentDetailView(DetailView):
    model = Student

class StudentDetailView1(DetailView):
    model = Student
    pk_url_kwarg = 'my_id'
    # template_name_suffix = '_jankari'
    template_name = 'myapp/student.html'

class StudentDetailView2(DetailView):
    model = Student
    template_name = 'myapp/student2.html'
    context_object_name = 'stu'

class StudentDetailView3(DetailView):
    model = Student
    template_name = 'myapp/student3.html'
    context_object_name = 'stu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all().order_by('name')
        return context