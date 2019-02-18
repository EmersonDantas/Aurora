from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from academic import views as academic_views
from academic import models as academic_models

@login_required
def showHorary(request):
    loggedStudent = academic_views.getLoggedStudent(request)
    periods = academic_models.Period.objects.filter(student=loggedStudent)
    context = {
        "periods":periods,
    }
    print(periods)
    return render(request, 'horary.html', context)
