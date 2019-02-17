from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from .views import showHorary

urlpatterns = [
    path('', include(home_urls), name='home'),
    path('horary/', showHorary, name='horary'),

]