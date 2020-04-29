from django import forms
from quack_forum.models import QuackForum
from quack_forum.models import CryptoQuack

#basic comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = QuackForum
        #exclude = ('user',)
        fields = ('comment',)
        labels = {
            'comment': 'Kvák'
        }

class CryptoForm(forms.ModelForm):
    publish_time = forms.DateField(input_formats=['%d.%m.%Y','%d. %m. %Y',])
    class Meta:
        model = CryptoQuack
        fields = ('tag','publish_time','cipher_unsolved','cipher_solved',)
