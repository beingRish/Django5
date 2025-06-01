from django.urls import path
from book.views import create_book

urlpatterns = [
    path('book/new', create_book, name='book-create'),
    
]
