from django.urls import path
from .views import BooksAPIView, AuthorRetrieveAPIView, TokenView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('books', BooksAPIView.as_view(), name='booksold-list-create'),
    path('books/<int:pk>', BooksAPIView.as_view(), name='delete-update'),
    path('authors/<int:pk>', AuthorRetrieveAPIView.as_view(), name='author-detail'),
    path('api/token', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh', TokenView.as_view(), name='token_refresh'),



]







