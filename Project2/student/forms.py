from django import forms

class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()

class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    key = forms.CharField(widget=forms.HiddenInput())

class Address(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.IntegerField()
