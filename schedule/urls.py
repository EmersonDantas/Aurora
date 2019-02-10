from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from .views import showSchedule, showSubjects, newPeriod, deletePeriod, editPeriod, editSubject, deleteSubject, newSubject

urlpatterns = [
    path('', include(home_urls), name='home'),
    path('schedule/', showSchedule, name='schedule'),
    path('schedule/newperiod/', newPeriod, name="newPeriod"),
    path('schedule/deleteperiod/', deletePeriod, name="deletePeriod"),
    path('schedule/editperiod/', editPeriod, name="editPeriod"),
    path('subject/<int:id>/', showSubjects, name='subject'),
    path('subject/editsubject/period=<int:periodId>/', editSubject, name='editSubject'),
    path('subject/deletesubject/period=<int:periodId>/', deleteSubject, name='deleteSubject'),
    path('subject/newsubject/period=<int:periodId>/', newSubject, name='newSubject'),
]