from django.urls import include,path
from quack_forum import views

app_name = 'quack_forum'
urlpatterns = [ path('',views.Comment,name = 'forum'),
                path('cryptoquack',views.CryptoComment,name = 'crypto_quack'),
                path('ciphers',views.CryptoForum, name = 'crypto_forum'),
                
]