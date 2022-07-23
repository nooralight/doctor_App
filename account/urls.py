from unicodedata import name
from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('registration/' , views.gotoRegistration, name= 'gotoRegistration'),
    path('create_user' , views.createUser, name= 'create-user'),
    path('login_user' , views.login, name= 'login-user'),
    path('login/' , views.gotoLogin, name= 'gotoLogin'),
    path('logout/' , views.logout, name= 'logout'),
]