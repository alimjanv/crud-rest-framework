from django.db import models
from django.contrib.auth.models import User

from src.books.models.author import Author


class Order(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending',
    )

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"