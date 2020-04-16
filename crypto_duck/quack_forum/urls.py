from django.urls import include,path
from quack_forum import views

app_name = 'quack_forum'
urlpatterns = [ path('',views.comment,name = 'forum'),
                
]