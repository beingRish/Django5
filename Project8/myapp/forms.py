from django import forms
from myapp.models import Student, Candidate

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'course']

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myname'}),
            'password': forms.PasswordInput(attrs={'class': 'mypass'}),
        }
