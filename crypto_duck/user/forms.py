from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
        help_texts = {
                    'username': None,
                }
        labels = {
            'username': 'Jméno týmu',
            'email': 'Email',
            'password': 'Heslo'
        }

class UserParticipantsForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('participant_one','participant_two','participant_three','participant_four')
        labels = {
            'participant_one': '1. hráč',
            'participant_two': '2. hráč',
            'participant_three': '3. hráč',
            'participant_four': '4. hráč',
        }
