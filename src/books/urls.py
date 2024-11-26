from django.urls import path
from .views import BooksAPIView, AuthorRetrieveAPIView

urlpatterns = [
    path('books', BooksAPIView.as_view(), name='booksold-list-create'),
    path('books/<int:pk>', BooksAPIView.as_view(), name='delete-update'),
    path('authors/<int:pk>', AuthorRetrieveAPIView.as_view(), name='author-detail'),
]


