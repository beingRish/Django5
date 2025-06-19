from django.shortcuts import render
from django.db.models import Count, Sum, Avg, F
from .models import Author, Book

def home(request):
    # # # Count the number of books each author has
    # authors = Author.objects.annotate(book_count = Count('book'))
    # print(authors)
    # print(vars(authors[1]))
    # authorBookCount = []
    # for author in authors:
    #     authorBookCount.append({
    #         'name': author.name,
    #         'book_count': author.book_count
    #     })
    # print(authorBookCount)
    # return render(request, 'myapp/home.html', {'authorBookCount': authorBookCount})
    
    
    # # Count the number of books each author has
    # # with related_name
    authors = Author.objects.annotate(book_count = Count('books'))
    authorBookCount = []
    for author in authors:
        authorBookCount.append({
            'name': author.name,
            'book_count': author.book_count
        })
    
    # # Total price of books for each author
    authors = Author.objects.annotate(total_price = Sum('books__price'), book_count = Count('books'))
    authorPriceCount = []
    authorBookCount = []

    for author in authors:
        authorBookCount.append({
            'name': author.name,
            'book_count': author.book_count
        })

    for author in authors:
        authorPriceCount.append({
            'name': author.name,
            'price_count': author.total_price
        })
    
    # # Calculate Final Price
    books = Book.objects.annotate(final_price = F('price') - F('discount'))
    BookFinalPrice = []
    for book in books:
        BookFinalPrice.append({
            'title': book.title,
            'final_price': book.final_price
        })

    
    # # Authors with more than 3 books
    book_filter = Author.objects.annotate(book_Filter=Count('books')).filter(book_Filter__gt=2)
    authorBook_Filter = []
    for book in book_filter:
        authorBook_Filter.append({
            'name': book.name,
            'book_Filter': book.book_Filter
        })

    # # Total book count and average price per author
    results = Book.objects.values('author__name').annotate(
        book_count = Count('id'),
        avg_price = Avg('price'),
    )

    for result in results:
        print(result['author__name'], result['book_count'], result['avg_price'])

    return render(request, 'myapp/home.html', {
        'authorBookCount': authorBookCount, 
        'authorPriceCount': authorPriceCount, 
        'BookFinalPrice': BookFinalPrice,
        'authorBook_Filter': authorBook_Filter,
        'results': results,
    })
