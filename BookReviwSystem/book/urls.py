from django.urls import path
from book.views import create_book, book_list

urlpatterns = [
    path('', book_list, name='book-list'),
    path('book/new', create_book, name='book-create'),
    
]
