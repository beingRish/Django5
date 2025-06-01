from django import forms
from book.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'genre', 'isbn', 'publication_date']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Title'
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter author name"
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter book description"
                }
            ),
            'genre': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'isbn': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter ISBN"
                }
            ),
            'publication_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }
        error_messages = {
            'title': {'required': 'Title is required'},
            'author': {'required': 'Author is required'},
            'description': {'required': 'Description is required'},
            'genre': {'required': 'Genre is required'},
            'isbn': {'required': 'ISBN is required'},
            'publication_date': {'required': 'Publication date is required'},
        }
