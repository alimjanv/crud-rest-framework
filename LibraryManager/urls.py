from django.urls import path
from .views import BooksAPIView, AuthorRetrieveAPIView

urlpatterns = [
    path('books/', BooksAPIView.as_view(), name='books-list-create'),
    path('books/<int:pk>/', BooksAPIView.as_view(), name='LibraryManager -delete-update'),

    path('authors/<int:pk>/', AuthorRetrieveAPIView.as_view(), name='author-detail'),
]


