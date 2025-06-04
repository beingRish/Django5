from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full mt-1 rounded-md shadow-sm bg-gray-700 text-white p-2 border border-gray-600'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full mt-1 rounded-md shadow-sm bg-gray-700 text-white p-2 border border-gray-600',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'class': 'block w-full mt-1 rounded-md shadow-sm bg-gray-700 text-white p-2 border border-gray-600'
            }),
        }


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price