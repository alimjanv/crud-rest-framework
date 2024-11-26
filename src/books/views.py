from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import BookSerializers, AuthorSerializers
from .models import Book, Author


class BooksAPIView(APIView):
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













