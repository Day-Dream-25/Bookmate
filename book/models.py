import datetime

from django.db import models


# Create your models here.
from user.models import User


class BookCategory(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.category)


class Books(models.Model):
    user = models.ManyToManyField("user.User", related_name='user_books')
    image = models.ImageField(blank=True, upload_to='images/')
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    publish_date = models.DateField()
    description = models.CharField(max_length=50)
    category = models.ForeignKey(BookCategory, null=True, on_delete=models.SET_NULL, related_name='category_book')
    state = models.ForeignKey('user.State',  null=True, on_delete=models.SET_NULL, related_name='book_state')
    city = models.ForeignKey('user.City', null=True, on_delete=models.SET_NULL, related_name='book_city')
    status = models.BooleanField()


class RequestBook(models.Model):
    book_status = (
        ("accepted", "accepted"),
        ("assigned", "assigned"),
        ("pending", "pending"),
        ("rejected", "rejected"),
        ("closed", "closed"),

    )

    date = models.DateTimeField(default=datetime.datetime.now())
    book_name = models.ForeignKey(Books, null=True, on_delete=models.SET_NULL, related_name='books_request')
    name = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='owner_book')
    status = models.CharField(
        max_length=20,
        choices=book_status, default="pending"
    )

