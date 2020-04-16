from django.shortcuts import render
from .forms import UserProfileForm, UserParticipantsForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def teams(request):
    teams = User.objects.all()
    context_teams = []
    for team in teams:
        if not team.is_superuser:
            context_teams.append(team)
    return render(request,'user/teams.html',{'context_teams':context_teams})

# User registration
def registration(request):
    
    user_registered = False
    error_flag = ''

    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)
        participants_form = UserParticipantsForm(data=request.POST)
        
        #profile validation
        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            participants = participants_form.save(commit = False)
            participants.user = user

            participants.save()

            user_registered = True

        else:
            error_flag = 'Error occured during validation!'
    
    else:
        user_form = UserProfileForm()
        participants_form = UserParticipantsForm()

    return render(request,'user/registration.html',{'user_registered':user_registered,
                                                    'error_flag':error_flag,
                                                    'user_form':user_form,
                                                    'participants_form':participants_form,})


# User login

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        #authentication
        user = authenticate(username=username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index_app:index'))
            
            else:
                return HttpResponse("Account not active!")
        else:
            return HttpResponse("Invalid login!")

    return render(request,"user/login.html")


#only user who is loged in can log out!
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index_app:index'))