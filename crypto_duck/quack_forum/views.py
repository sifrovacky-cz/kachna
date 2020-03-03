from django.shortcuts import render
# importing comment form from .forms
from quack_forum.forms import CommentForm
from quack_forum.models import QuackForum

# Create your views here.

# saves comment and returns comment models from database
def comment(request):
    
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
        form = CommentForm()

    # Ordering comments from oldest to newest
    comment_list = QuackForum.objects.order_by('date_time')


    return render(request,'quack_forum/forum.html',{'form':form,'comment_list':comment_list,})
