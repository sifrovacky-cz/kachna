from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
# importing comment form from .forms
from quack_forum.forms import CommentForm
from quack_forum.models import QuackForum

# Create your views here.

# saves comment and returns comment models from database

def comment(request):
    #error (for unregistred user, if they do the check wrong)    
    error_flag = ''

    #checking if user is loged in
    if request.user.is_authenticated:
        html_path = 'quack_forum/forum.html'    
        form = CommentForm()

        if request.method == "POST":
            form = CommentForm(request.POST)
            
            if form.is_valid():
                form_with_user = form.save(commit=False)
                form_with_user.user = request.user.username
                form_with_user.save()
            form = CommentForm()

    # this is the part when user is not loged in
    else:
        
        check_password = "kachna19"
        html_path = 'quack_forum/forum_unauthorized.html'
        
        form = CommentForm()

        if request.method == "POST":
            form = CommentForm(request.POST)
            
            if form.is_valid() and request.POST.get('check') == check_password:
                form_with_user = form.save(commit=False)
                form_with_user.user = request.POST.get('username')
                form_with_user.save()
            else:
                error_flag = "Please write " + check_password + " into the box above!"
            form = CommentForm()

    # Ordering comments from oldest to newest
    comment_list = QuackForum.objects.order_by('-date_time')


    return render(request,html_path,{'form':form,'comment_list':comment_list,'error_flag':error_flag})
