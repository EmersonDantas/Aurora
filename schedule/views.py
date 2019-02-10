from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user import models as user_models
from .models import Period, Subject, Note
from .forms import PeriodForm

@login_required
def showSchedule(request):
        student = getLoggedStudent(request)

        if(isinstance(student, user_models.Student)):
                studentAllPeriods = Period.objects.filter(student=student)
                return render(request, 'schedule.html', {'periods':studentAllPeriods})

@login_required
def showSubjects(request, id):
        periodSelected = get_object_or_404(Period, pk=id)

        student = getLoggedStudent(request)

        allSubjectsOfThisPeriod = Subject.objects.filter(period=periodSelected, student=student)
        
        if(allSubjectsOfThisPeriod.first() != None):
                return render(request, 'subjects.html', {'subjects':allSubjectsOfThisPeriod})
        else:
                return redirect('schedule')

@login_required
def getLoggedStudent(request):
        userDjango = request.user
        userAurora = user_models.User.objects.get(user=userDjango)
        student = user_models.Student.objects.get(user=userAurora)
        return student

@login_required
def newPeriod(request):
        form = PeriodForm(request.POST or None)
        if(request.method == 'POST'):
                if(form.is_valid()):
                        year = form.cleaned_data['year']
                        student = getLoggedStudent(request)
                        newPeriod = Period(year=year, student=student)
                        newPeriod.save()

        return redirect('schedule')

@login_required
def deletePeriod(request):
        if(request.method == 'POST'):
                id = request.POST.get('id')
                loggedStudent = getLoggedStudent(request)
                periodSelected = get_object_or_404(Period, pk=id, student=loggedStudent)
                print(periodSelected)
                periodSelected.delete()
        return redirect('schedule')
                