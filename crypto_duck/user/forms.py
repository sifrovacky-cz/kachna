from django import forms
from .models import UserProfile, MyUser
from django.contrib.auth.forms import UserChangeForm

class UserProfileForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label = 'Heslo')
    email = forms.EmailField(required = True)
    password_check = forms.CharField(widget = forms.PasswordInput(), label = 'Heslo znovu')

    class Meta():
        model = MyUser
        fields = ('username','email','password','password_check')
        help_texts = {
                    'username': None,
                }
        labels = {
            'username': 'Jméno týmu',
            'email': 'Email',
            #password and password_check were not working, labels were moved up
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

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = True)
    class Meta():
        model = MyUser
        fields = ('username','email')
        labels = {
            'username': 'Jméno týmu',
            'email': 'Email',
        }

class PasswordUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label = 'Heslo')
    password_check = forms.CharField(widget = forms.PasswordInput(), label = 'Heslo znovu')
    class Meta():
        model = MyUser
        fields = ('password','password_check')

class UserInfoForm(UserChangeForm):
    password = None
    class Meta:
        model = MyUser
        fields = ('username','email')
        labels = {
            'username': 'Jméno týmu',
            'email': 'Email',
        }