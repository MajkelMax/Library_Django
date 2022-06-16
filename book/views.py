from django.shortcuts import render
from .models import Book
from .filters import OrderFilter
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def book_list(request):
    books = Book.objects.all()

    myFilter = OrderFilter(request.GET, queryset=books)
    books = myFilter.qs

    context = {'books': books, 'myFilter': myFilter}
    return render(request, 'book/home.html', context)


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'


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
