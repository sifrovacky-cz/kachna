from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# importing comment form from .forms
from quack_forum.forms import CommentForm
from quack_forum.models import QuackForum

# Create your views here.

# saves comment and returns comment models from database

def comment(request):
    
    #checking if user is loged in
    if request.user.is_authenticated:
            
        form = CommentForm()

        if request.method == "POST":
            form = CommentForm(request.POST)
            

            if form.is_valid():
                form_with_user = form.save(commit=False)
                form_with_user.user = request.user.username
                form_with_user.save()
            form = CommentForm()

        # Ordering comments from oldest to newest
        comment_list = QuackForum.objects.order_by('date_time')


        return render(request,'quack_forum/forum.html',{'form':form,'comment_list':comment_list,})
    
    # this is the part when user is not loged in
    else:
        
        form = CommentForm()

        if request.method == "POST":
            form = CommentForm(request.POST)
            

            if form.is_valid():
                form_with_user = form.save(commit=False)
                form_with_user.user = request.POST.get('username')
                form_with_user.save()
            form = CommentForm()

        # Ordering comments from oldest to newest
        comment_list = QuackForum.objects.order_by('-date_time')


        return render(request,'quack_forum/forum_unauthorized.html',{'form':form,'comment_list':comment_list,})
