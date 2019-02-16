from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from .views import showAcademic, showSubjects, newPeriod, deletePeriod, editPeriod, editSubject, deleteSubject, newSubject, newNote, deleteNote, editNote

urlpatterns = [
    path('', include(home_urls), name='home'),
    path('academic/', showAcademic, name='academic'),
    path('academic/newperiod/', newPeriod, name="newPeriod"),
    path('academic/deleteperiod/', deletePeriod, name="deletePeriod"),
    path('academic/editperiod/', editPeriod, name="editPeriod"),
    path('subject/periodid=<int:id>/', showSubjects, name='subject'),
    path('subject/editsubject/period=<int:periodId>/', editSubject, name='editSubject'),
    path('subject/deletesubject/period=<int:periodId>/', deleteSubject, name='deleteSubject'),
    path('subject/newsubject/period=<int:periodId>/', newSubject, name='newSubject'),
    path('subject/newnote/period=<int:periodId>/', newNote, name='newNote'),
    path('subject/deletenote/period=<int:periodId>/', deleteNote, name='deleteNote'),
    path('subject/editnote/period=<int:periodId>/', editNote, name='editNote'),
]