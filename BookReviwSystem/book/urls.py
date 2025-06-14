from django.urls import path
from book.views import create_book, book_list, book_detail, book_update, book_delete

urlpatterns = [
    path('', book_list, name='book-list'),
    path('book/new/', create_book, name='book-create'),
    path('book/<int:pk>/', book_detail, name='book-detail'),
    path('book/<int:pk>/edit/', book_update, name='book-update'),
    path('book/<int:pk>/delete/', book_delete, name='book-delete'),
]
