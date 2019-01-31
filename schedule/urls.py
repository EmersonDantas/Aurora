from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from .views import showSchedule 

urlpatterns = [
    path('', include(home_urls), name='home'),
    path('schedule/', showSchedule, name='schedule'),
]