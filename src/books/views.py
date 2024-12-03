from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers.author import AuthorSerializers
from .serializers.book import BookSerializers
from .models.author import Author
from .models.book import Book


class BooksAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, pk=None):
            if pk:
                book = get_object_or_404(Book, pk=pk)
                serializer = BookSerializers(book)
                return Response(serializer.data)
            else:
                books = Book.objects.all()
                serializer = BookSerializers(books, many=True)
                return Response(serializer.data)

    def post(self, request):

        request.data['author'] = request.user.id
        serializer = BookSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
            book = get_object_or_404(Book, pk=pk)
            serializer = BookSerializers(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
            book = get_object_or_404(Book, pk=pk)
            print(request.user)

            if book.author != request.user:
                return Response({"detail": "Siz faqat o'z kitoblaringizni o'chira olasiz."},
                                status=status.HTTP_403_FORBIDDEN)

            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorRetrieveAPIView(APIView):

        def get(self, request, pk):
            author = get_object_or_404(Author, pk=pk)
            serializer = AuthorSerializers(author)
            return Response(serializer.data)




def author_books(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
        books = author.books.all()
        books_data = [{"title": book.title, "subtitle": book.subtitle, "price": book.price} for book in books]
        return JsonResponse({"author": author.name, "books": books_data})
    except Author.DoesNotExist:
        return JsonResponse({"error": "Muallif topilmadi"}, status=404)
