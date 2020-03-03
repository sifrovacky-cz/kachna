from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#User profile model, one to one relation to User model

class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) # check if on_delete = models.CASCADE is suitable
    

    def __str__(self):
        return self.user.username
