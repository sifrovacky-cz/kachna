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
    #publish_time = forms.DateField(input_formats=['%d.%m.%Y','%d. %m. %Y',])
    class Meta:
        model = CryptoQuack
        fields = ('tag','cipher_unsolved','cipher_solved',)
        labels = {
            'tag': 'Krátký popisek',
            'cipher_unsolved':'Toto uvidí všichni hned',
            'cipher_solved':'Toto uvidí všichni až po datu nastaveném adminem'
        }