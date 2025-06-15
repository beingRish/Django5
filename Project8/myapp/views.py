from django.shortcuts import render, HttpResponse
from django.views import View
from myapp.models import Student, Candidate 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from myapp.forms import StudentForm, ContactForm, CandidateForm
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django import forms

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
    

# Form View
class ContactFormView(FormView):
    template_name = 'myapp/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'
    initial = {'name': 'Sonam', 'email': 'sonam@example.com'}

    def form_valid(self, form):
        # print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
        # return HttpResponse('Thank You form submitted !!')
    

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with your form submission.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra"] = 'Hello FormView'
        return context
    
class StudentFormView(FormView):
    template_name = 'myapp/register.html'
    form_class = StudentForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        roll = form.cleaned_data['roll']
        course = form.cleaned_data['course']
        student = Student(
            name = name,
            roll = roll,
            course = course
        )
        student.save()
        return HttpResponse('Thank You form submitted !!')
    

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with your form submission.')
        return super().form_valid(form)
    

# Create View
# class CandidateCreateView(CreateView):
#     model = Candidate
#     fields = ['name', 'email', 'password']
#     # success_url = '/thanks/'
#     template_name = 'myapp/candidate_register.html'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class': 'myname'})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class': 'mypass'})
#         return form
    

class CandidateCreateView(CreateView):
    form_class = CandidateForm
    template_name = 'myapp/candidate_register.html'
    # success_url = '/thanks/'


# Update View
# class CandidateUpdateView(UpdateView):
#     model = Candidate
#     fields = ['name', 'email', 'password']
#     template_name = 'myapp/candidate_register.html'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class': 'myname'})
#         form.fields['password'].widget = forms.PasswordInput(render_value=True, attrs={'class': 'mypass'})
#         return form

class CandidateUpdateView(UpdateView):
    model = Candidate
    form_class = CandidateForm
    template_name = 'myapp/candidate_register.html'
