from django.urls import path, include
from home.views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register, name='register')
]