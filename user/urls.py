from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from .views import logoutUser, registerUser
from django.contrib.auth import views as auth_views
from academic import urls as academic_urls

urlpatterns = [
    path('', include(home_urls), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
    path('', include(academic_urls), name='academic'),
]
