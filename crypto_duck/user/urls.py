from django.urls import include,path
from user import views

app_name = 'user'
urlpatterns = [ path('register/',views.registration,name = 'registration'),
                path('login/',views.user_login,name='user_login'),
                
                ]