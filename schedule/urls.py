from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from .views import showSchedule, showSubjects, newPeriod, deletePeriod

urlpatterns = [
    path('', include(home_urls), name='home'),
    path('schedule/', showSchedule, name='schedule'),
    path('subject/<int:id>/', showSubjects, name='subject'),
    path('schedule/newperiod/', newPeriod, name="newPeriod"),
    path('schedule/deleteperiod/', deletePeriod, name="deletePeriod"),
]