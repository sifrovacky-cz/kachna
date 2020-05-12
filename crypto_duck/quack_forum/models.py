from django.db import models
from django.conf import settings
import datetime

# Create your models here.
# Basic comment database model, includes time, author and comment text
# change author from text input to user profile name, when user exists
class QuackForum(models.Model):
    comment = models.TextField(max_length=300)
    user = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class CryptoQuack(models.Model):
    publish_time = models.DateField()
    tag = models.CharField(max_length=100)
    cipher_unsolved = models.FileField(upload_to='crypto_quack_unsolved')
    cipher_solved = models.FileField(upload_to='crypto_quack_solved')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author) + ": " + str(self.tag)