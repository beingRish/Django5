from django import forms
from django.core.validators import MinLengthValidator, RegexValidator

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')

        if name_value and len(name_value) < 4:
            self.add_error('name', 'Enter more than or equal 4 chars')
        
        if email_value and len(email_value) < 10:
            self.add_error('email', 'Enter more than or equal 10 chars')

        return cleaned_data


class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    key = forms.CharField(widget=forms.HiddenInput())

class Address(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.IntegerField()

# Field Type Examples
class DemoForm(forms.Form):
    # Basic Fields
    name = forms.CharField()
    email = forms.EmailField()
    pin_code = forms.IntegerField()

    # Additional Field Types
    age = forms.FloatField()
    date_of_birth = forms.DateField()
    appointment_time = forms.TimeField()
    appointment_datetime = forms.DateTimeField()
    is_subscribed = forms.BooleanField()
    agree_terms = forms.NullBooleanField()

    # Choice Fields
    gender = forms.ChoiceField(choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('o', 'Other')
    ])
    interests = forms.MultipleChoiceField(choices=[
        ('tech', 'Technology'),
        ('art', 'Art'),
        ('sports', 'Sports')
    ])

    # File and URL Fields
    profile_image = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()

    # Other Specialized Fileds
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    password = forms.CharField(widget=forms.PasswordInput())
    slug = forms.SlugField()
    ip_address = forms.GenericIPAddressField()
    rating = forms.DecimalField()

    # Field Arguments Example
