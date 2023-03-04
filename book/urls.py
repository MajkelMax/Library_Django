from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list, name='book-home'),
    path('new/', views.BookCreateView.as_view(), name='book-form'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('search_books/', views.book_search, name='book-search'),
]