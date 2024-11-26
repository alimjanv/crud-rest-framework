from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="booksold")
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title

