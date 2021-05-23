from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Author(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):

        return self.username

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True,blank=True)
    book_name = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.book_name


