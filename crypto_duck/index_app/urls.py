from django.urls import include,path
from index_app import views

app_name = "index_app"
urlpatterns = [ path('',views.index,name = 'index'),
                path('info/',views.info,name='info'),
                path('results/',views.results,name='results'),
                path('rules/',views.rules,name='rules'),
                
                ]
