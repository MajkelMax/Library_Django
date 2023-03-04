from django.shortcuts import render
import requests
from .api import services
from .models import Book
from django.views.generic import (CreateView, DetailView,
                                  DeleteView, UpdateView)
from .forms import BookForm

def api_search(request):
    return render(request, 'book/api_book_search.html')

def api_search_results(request):
    search = request.GET['search']
    response = f'https://www.googleapis.com/books/v1/volumes?q={search}'
    result = requests.get(response).json()
    context = {'response': result}

    return render(request, 'book/api_book_search_results.html', context)

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

    return render(request, 'book/api_book_details.html', context)


def book_list(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'book/home.html', context)


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    success_url = '/'


class BookDetailView(DetailView):
    model = Book


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/'


class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)
