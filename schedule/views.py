from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user import models as user_models
from .models import Period, Subject, Note

@login_required
def showSchedule(request):
        userDjango = request.user
        userAurora = user_models.User.objects.get(user=userDjango)
        student = user_models.Student.objects.get(user=userAurora)

        if(isinstance(student, user_models.Student)):
                studentAllPeriods = Period.objects.filter(student=student)
                return render(request, 'schedule.html', {'periods':studentAllPeriods})

@login_required
def showSubjects(request, id):
        periodSelected = get_object_or_404(Period, pk=id)
        allSubjectsOfThisPeriod = Subject.objects.filter(period=periodSelected)
        
        if(allSubjectsOfThisPeriod.first() != None):
                print("Não é nulo")
                return render(request, 'subjects.html', {'subjects':allSubjectsOfThisPeriod})
        else:
                return redirect('schedule')