from django.contrib.auth.models import AbstractUser
from django.db import models


class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_city')
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class User(AbstractUser):
    phone_no = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=50, blank=True)
    state = models.ForeignKey('user.State', null=True, on_delete=models.SET_NULL, related_name='user_state')
    city = models.ForeignKey('user.City', null=True, on_delete=models.SET_NULL, related_name='user_city')

    def __str__(self):
        return str(self.username)
