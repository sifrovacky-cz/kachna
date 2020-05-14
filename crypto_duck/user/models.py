from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _    

class MyValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+\- ]+$'

class MyUser(AbstractUser):
    username_validator = MyValidator()
    username = models.CharField(
        _('username'),
        max_length=100,
        unique=True,
        help_text=_('Povinné. Maximálně 100 znaků!'),
        validators=[username_validator],
            error_messages={
            'unique': _("Tento uživatel již existuje."),
        },
    )
    class Meta:
        verbose_name = "tým"
        verbose_name_plural = "Týmy"

#User profile model, one to one relation to User model
#Note: User = team, participants = team members
class UserProfile (models.Model):
    user = models.OneToOneField(MyUser, on_delete = models.CASCADE)
    
    #participants
    participant_one = models.CharField(max_length=100)
    participant_two = models.CharField(max_length=100,blank=True)
    participant_three = models.CharField(max_length=100,blank=True)
    participant_four = models.CharField(max_length=100,blank=True)

    class Meta:
        verbose_name = "soupiska"
        verbose_name_plural = "Soupisky"

    def __str__(self):
        return self.user.username

class UserInfo (models.Model):
    user = models.OneToOneField(MyUser, on_delete = models.CASCADE)
    account = models.CharField(max_length=50,blank=True)
    variable_symbol = models.CharField(max_length=50,blank = True)

    class Meta:
        verbose_name = "platební údaj"
        verbose_name_plural = "Platební údaje"

    @classmethod
    def create(self, user_info):
        return self(user = user_info)
        
    def __str__(self):
        return self.user.username

