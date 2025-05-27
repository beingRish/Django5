from django import forms
from student.models import User

class Registration(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)
    confirm_password = forms.CharField()
    class Meta:
        model = User
        # fields = ['name', 'email', 'password']
        fields = '__all__'
        labels = {
            'name': "Enter Name",
            'email': "Enter Email",
            'password': "Enter Password"
        }
        error_messages = {
            'email': {
                'required': "Email is required",
            },
            'name': {
                'required': "Name is required",
            },
            'password': {
                'required': "Password is required",
            }
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'pwdclass'}),
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Enter your name'})
        }