from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserParticipantsForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('participant_one','participant_two','participant_three','participant_four')
