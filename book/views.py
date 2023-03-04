from django.shortcuts import render
from .models import Book
from django.views.generic import (CreateView, DetailView,
                                  DeleteView, UpdateView)
from .forms import BookForm


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
