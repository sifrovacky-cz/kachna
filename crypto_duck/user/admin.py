from django.contrib import admin
from .models import UserProfile,MyUser,UserInfo
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(MyUser)
admin.site.register(UserInfo)