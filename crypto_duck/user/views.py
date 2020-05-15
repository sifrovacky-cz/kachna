from django.shortcuts import render
from .forms import UserProfileForm, UserParticipantsForm, UserInfoForm, PasswordUpdateForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from .models import UserProfile,MyUser,UserInfo
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from index_app.models import DisplayModel
import datetime

# Create your views here.

def teams(request):
    teams = UserProfile.objects.all()
    context_teams = []
    for team in teams:
        if not team.user.is_superuser:
            context_teams.append(team)
    return render(request,'user/teams.html',{'context_teams':context_teams})

# User registration
def registration(request):
    #get visibility
    if DisplayModel.objects.filter(title = "Účty").first():
        visible = DisplayModel.objects.get(title = "Účty").date<= datetime.date.today()
    else:
        visible = True
    user_registered = False
    error_flag = ''

    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)
        participants_form = UserParticipantsForm(data=request.POST)

        #profile validation
        if user_form.is_valid():
            if user_form.cleaned_data['password'] == user_form.cleaned_data['password_check']:
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                participants = participants_form.save(commit = False)
                participants.user = user
                participants.save()

                user_info = UserInfo.create(user)
                user_info.save()

                user_registered = True
                login(request, user)
            else:
                error_flag = 'Hesla se neshodují!'

        else:
            error_flag = 'Nastal problém během validace!'

    else:
        user_form = UserProfileForm()
        participants_form = UserParticipantsForm()

    return render(request,'user/registration.html',{'user_registered':user_registered,
                                                    'error_flag':error_flag,
                                                    'user_form':user_form,
                                                    'participants_form':participants_form,
                                                    'visible':visible})

# User login
def user_login(request):
    #get visibility
    if DisplayModel.objects.filter(title = "Účty").first():
        visible = DisplayModel.objects.get(title = "Účty").date<= datetime.date.today()
    else:
        visible = True
    error_flag = ''
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
                error_flag = 'Účet není aktivní!'
        else:
            error_flag = 'Přihlašovací údaje nejsou v pořádku!'

    return render(request,"user/login.html",{'error_flag': error_flag,
                                            'visible':visible,})

#only user who is loged in can log out!
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index_app:index'))


### unused, does not work properly
@login_required
def update_page(request):
    error_flag = ''
    participants_model = UserProfile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserUpdateForm(data=request.POST, instance=request.user)
        participants_form = UserParticipantsForm(data=request.POST, instance = participants_model)
        password_form = PasswordUpdateForm(instance = request.user, data = request.POST)

        #profile validation
        if user_form.is_valid() and participants_form.is_valid():

            error_flag = 'Data byla uložena.'
            if password_form.is_valid() and password_form.cleaned_data['password']:
                if password_form.cleaned_data['password'] == password_form.cleaned_data['check_password']:
                    
                    user = user_form.save(commit = False)
                    user.set_password(password_form.cleaned_data['password'])
                    user.save()

                    participants = participants_form.save(commit = False)
                    participants.user = user
                    participants.save()

                    error_flag = 'Data byla uložena. Nové heslo bylo nastaveno.'
                else:
                    error_flag = 'Hesla se neshodují!'
            else: 
                password = request.user.password
                user = user_form.save()

                user.save()
                user.set_password(password)
                #user.save()

                participants = participants_form.save(commit = False)
                participants.user = user
                participants.save()

                error_flag = 'Data byla uložena. Heslo nebylo změněno.'

        else:
            error_flag = 'Nastal problém během validace!'

        login(request, user)
    else:
        user_form = UserUpdateForm(instance=request.user)
        participants_form = UserParticipantsForm(instance=participants_model)
        password_form = PasswordUpdateForm()
    return render(request,'user/profile_update.html',{'user_form': user_form,
                                                    'participants_form': participants_form,
                                                    'password_form': password_form,
                                                    'error_flag': error_flag, })

@login_required
def profile_page(request):
    user_info_model = UserInfo.objects.get(user = request.user)
    return render(request,'user/profile_page.html',{'info':user_info_model})

@login_required
def profile_info_update(request):
    participants_model = UserProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance = request.user)
        profile_form = UserParticipantsForm(request.POST, instance = participants_model)
        if form.is_valid():
            form.save()
            user = form.save()
            profile_form.save(commit =False)
            profile_form.user = user
            profile_form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('user:profile_page'))
    else:
        form = UserInfoForm(instance = request.user)
        profile_form = UserParticipantsForm(instance = participants_model)
    
    return render(request,'user/profile_info_update.html',{'form':form,
                                                            'profile_form':profile_form})

@login_required
def profile_password_update(request):
    flag = ''
    if request.method == 'POST':
        form = PasswordUpdateForm(data = request.POST, instance = request.user)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                user = request.user
                user.set_password(form.cleaned_data['password'])
                user.save()
                update_session_auth_hash(request, user)
                return HttpResponseRedirect(reverse('user:profile_page'))
            else:
                flag = 'Hesla se neshodují.'
        else:
            flag = 'Heslo nebylo změněno.'
    else:
        form = PasswordUpdateForm(instance = request.user)
    return render(request,'user/profile_password_update.html',{'form':form,'flag':flag})