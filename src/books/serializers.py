from rest_framework import serializers

from .models import Book, Author


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'price')


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'age')

