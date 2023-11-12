from django.urls import path
from .views import (BookListView, BookCreateView, BookDetailView, BookDeleteView, BookUpdateView, UserBooksView,
                    subscribe, UserCreateView)

urlpatterns = [
    path('api/', BookListView.as_view(), name='book-list'),
    path('api/all/', BookListView.as_view(), name='book-list-all'),
    path('api/new/', BookCreateView.as_view(), name='book-create'),
    path('api/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('api/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('api/my-books/', UserBooksView.as_view(), name='user-books'),
    path('api/subscribe/', subscribe, name='subscribe'),
    path('signup/', UserCreateView.as_view(), name='signup'),
]

