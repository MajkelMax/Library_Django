from django.shortcuts import render
from .models import Book
from django.views.generic import (CreateView, DetailView,
                                  DeleteView, UpdateView)
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'book/home.html', context)

def book_search(request):
    q = request.POST['query']
    books = Book.objects.filter(title__contains=q)
    return render(request, 'book/search_books.html', {'books':books})


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
