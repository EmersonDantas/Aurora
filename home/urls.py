from django.contrib import admin
from django.urls import path
from .views import index, loginUser, logoutUser
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logoutUser, name='logout'),
]
