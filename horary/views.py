from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from academic import views as academic_views
from academic import models as academic_models
import re

@login_required
def showHorary(request):
    loggedStudent = academic_views.getLoggedStudent(request)
    periods = academic_models.Period.objects.filter(student=loggedStudent)

    if(request.method == 'POST'):
        optionSelected = request.POST.get('period-selected')
        optionList = optionSelected.split('-')
        periodSelectedId = int(optionList[1])

        periodSelected = get_object_or_404(academic_models.Period, pk=periodSelectedId, student=loggedStudent)
        print(periodSelected)
        
        periods = academic_models.Period.objects.filter(student=loggedStudent)
        allSubjectsOfThisPeriod = []
        allSubjectsOfThisPeriod = academic_models.Subject.objects.filter(period=periodSelected, student=loggedStudent)
        context = {
            "currentPeriod":periodSelected,
            "periods":periods,
            "subjects":allSubjectsOfThisPeriod,
        }
    else:
        lastRegistredPeriod = None
        allSubjectsOfThisPeriod = []
        if(len(periods) > 0):
            lastRegistredPeriod = periods[len(periods)-1]
            allSubjectsOfThisPeriod = academic_models.Subject.objects.filter(period=lastRegistredPeriod, student=loggedStudent)

        context = {
            "currentPeriod":lastRegistredPeriod,
            "periods":periods,
            "subjects":allSubjectsOfThisPeriod,
        }
    
    return render(request, 'horary.html', context) 