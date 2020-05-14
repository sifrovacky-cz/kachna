from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from index_app.models import DisplayModel
import datetime

#form and model of normal comment
from quack_forum.forms import CommentForm
from quack_forum.models import QuackForum

#form and model of crypto comment
from quack_forum.forms import CryptoForm
from quack_forum.models import CryptoQuack

# saves comment and returns comment models from database

def Comment(request):
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
        
        check_password = "TBD"
        html_path = 'quack_forum/forum_unauthorized.html'
        
        form = CommentForm()

        if request.method == "POST":
            form = CommentForm(request.POST)
            
            if form.is_valid() and request.POST.get('check') == check_password:
                if request.POST.get('username'):
                    form_with_user = form.save(commit=False)
                    form_with_user.user = request.POST.get('username')
                    form_with_user.save()
                else:
                    error_flag = "Napište prosím přezdívku, pod kterou chcete příspěvek přidat!"
            else:
                error_flag = "Napište prosím" + check_password + " do příslušného políčka!"
            form = CommentForm()

    # Ordering comments from oldest to newest
    comment_list = QuackForum.objects.order_by('-date_time')


    return render(request,html_path,{'form':form,'comment_list':comment_list,'error_flag':error_flag})


@login_required
def CryptoComment(request):
    form = CryptoForm()

    if request.method == 'POST':
        form = CryptoForm(request.POST,request.FILES)

        if form.is_valid():
            form = form.save(commit = False)
            form.author = request.user
            form.save()
            return HttpResponseRedirect(reverse('quack_forum:crypto_forum'))

    return render(request,'quack_forum/crypto_comment_form.html',{'form':form,
                                                                    })


def CryptoForum(request):
    #get visibility
    if DisplayModel.objects.filter(title = "Šifry").first():
        visible = DisplayModel.objects.get(title = "Šifry").date<= datetime.date.today()
    else:
        visible = True
    today =  datetime.date.today()
    error_flag = ""

    if request.method == 'POST':
        try:
            id_value = request.POST.get('id_value')
            CryptoQuack.objects.filter(id=id_value).delete()
        except:
            error_flag = "An error has occured :("

    cryptoCommentList = CryptoQuack.objects.order_by('-publish_time')


    return render(request,'quack_forum/ciphers_try.html',{'cryptoComentList':cryptoCommentList,
                                                    'today':today,
                                                    'error_flag':error_flag,
                                                    'visible':visible
                                                    })






