from django.shortcuts import render
from .forms import UserProfileForm
# Create your views here.

def index(request):
    return render(request,'index.html')

def registration(request):
    
    user_registered = False
    error_flag = ''

    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)
        
        #profile validation
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_registered = True

        else:
            error_flag = 'Error occured during validation!'
    
    else:
        user_form = UserProfileForm()

    return render(request,'user/registration.html',{'user_registered':user_registered,
                                                    'error_flag':error_flag,
                                                    'user_form':user_form})



# work in progress
def login(request):
    return render(request,'user/login.html')