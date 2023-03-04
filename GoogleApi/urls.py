from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_search, name='api-book-search'),
    path('books_results/', views.api_search_results, name='books_results'),
    path('books_results/book_details/', views.api_search_book_details, name='book_details'),
]