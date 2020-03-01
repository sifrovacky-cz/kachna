from django.urls import include,path
from quack_forum import views

urlpatterns = [ path('',views.comment,name = 'quack_forum'),
                
]