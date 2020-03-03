from django import forms
from quack_forum.models import QuackForum

#basic comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = QuackForum
        fields = ('user','comment')