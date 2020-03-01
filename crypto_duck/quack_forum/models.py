from django.db import models
import datetime

# Create your models here.
# Basic comment database model, includes time, author and comment text
# change author from text input to user profile name, when user exists
class QuackForum(models.Model):
    comment = models.CharField(max_length=300)
    user = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment