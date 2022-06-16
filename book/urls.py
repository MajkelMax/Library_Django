from django.urls import path
from .views import (BookCreateView,BookDetailView,
                    BookDeleteView,BookUpdateView,)
from . import views


urlpatterns = [
    path('', views.book_list, name='book-home'),
    path('new/', BookCreateView.as_view(), name='book-form'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
]