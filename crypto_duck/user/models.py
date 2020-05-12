from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#User profile model, one to one relation to User model
#Note: User = team, participants = team members
class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    #participants
    participant_one = models.CharField(max_length=100)
    participant_two = models.CharField(max_length=100,blank=True)
    participant_three = models.CharField(max_length=100,blank=True)
    participant_four = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

