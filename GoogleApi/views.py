from django.shortcuts import render
import requests
from book.models import Book
from book.views import book_list


def api_search(request):
    return render(request, 'GoogleApi/api_book_search.html')


def api_search_results(request):
    search = request.GET['search']
    response = f'https://www.googleapis.com/books/v1/volumes?q={search}'
    result = requests.get(response).json()
    context = {'response': result}

    return render(request, 'GoogleApi/api_book_search_results.html', context)


def api_search_book_details(request):
    book = request.GET['book_info']
    book = requests.get(book).json()
    res_title = book['volumeInfo']['title']
    res_authors = book['volumeInfo']['authors'][0]
    res_published_date = book['volumeInfo']['publishedDate']
    res_isbn = book['volumeInfo']['industryIdentifiers'][0]['identifier']
    res_page_count = book['volumeInfo']['pageCount']
    res_language = book['volumeInfo']['language']

    if request.method == "POST":
        if len(res_published_date) < 5:
            res_published_date += "-01-01"
        x = Book(title=res_title, author=res_authors,
                 pub_date=res_published_date, isbn=res_isbn,
                 pages=res_page_count, language=res_language)
        Book.save(x)
        return book_list(request)

    context = {'book': book}

    return render(request, 'GoogleApi/api_book_details.html', context)
