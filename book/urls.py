from django.urls import path
from .views import (BookCreateView, BookDetailView,
                    BookDeleteView, BookUpdateView,
                    api_search, api_search_results,
                    api_search_book_details)
from .import views


urlpatterns = [
    path('', views.book_list, name='book-home'),
    path('new/', BookCreateView.as_view(), name='book-form'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('search/', api_search, name='api-book-search'),
    path('search/books_results', api_search_results, name='books_results'),
    path('search/book_details', api_search_book_details, name='book_details'),
]