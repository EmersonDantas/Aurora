from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user import models as user_models
from .models import Period, Subject, Note
from .forms import PeriodForm, SubjectForm, NoteForm

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
        allNotesOfThisSubject = Note.objects.filter(period=periodSelected)

        context = {
                'subjects':allSubjectsOfThisPeriod, 
                'periodId':id,
                'allNotes':allNotesOfThisSubject,
                'period':periodSelected
                }
        return render(request, 'subjects.html', context)

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
                periodSelected.delete()
                
        return redirect('schedule')

@login_required
def editPeriod(request):
        if(request.method == 'POST'):
                id = request.POST.get('id')
                year = request.POST.get('year')
                loggedStudent = getLoggedStudent(request)
                periodSelected = get_object_or_404(Period, pk=id, student=loggedStudent)
                periodSelected.year = year
                periodSelected.save()

        return redirect('schedule')

@login_required
def editSubject(request, periodId):
        if(request.method == 'POST'):
                loggedStudent = getLoggedStudent(request)
                periodSelected = get_object_or_404(Period, pk=periodId, student=loggedStudent)

                id = request.POST.get('id')
                name = request.POST.get('name')
                credits = request.POST.get('credits')
                subjectSelected = get_object_or_404(Subject, pk=id, period=periodSelected)
                subjectSelected.name = name
                subjectSelected.credits = credits
                subjectSelected.save()

        return redirect('subject', periodId)

@login_required
def deleteSubject(request, periodId):
        if(request.method == 'POST'):
                loggedStudent = getLoggedStudent(request)
                periodSelected = get_object_or_404(Period, pk=periodId, student=loggedStudent)

                id = request.POST.get('id')
                subjectSelected = get_object_or_404(Subject, pk=id, period=periodSelected)
                subjectSelected.delete()

        return redirect('subject', periodId)

@login_required
def newSubject(request, periodId):
        form = SubjectForm(request.POST or None)
        if(request.method == 'POST'):
                if(form.is_valid()):
                        loggedStudent = getLoggedStudent(request)
                        periodSelected = get_object_or_404(Period, pk=periodId, student=loggedStudent)

                        name = form.cleaned_data['name']
                        credits = form.cleaned_data['credits']

                        newSubject = Subject(name=name, credits=credits, period=periodSelected, student=loggedStudent)
                        newSubject.save()

        return redirect('subject', periodId)

@login_required
def newNote(request, periodId):
        form = NoteForm(request.POST or None)
        if(request.method == 'POST'):
                if(form.is_valid()):
                        loggedStudent = getLoggedStudent(request)
                        periodSelected = get_object_or_404(Period, pk=periodId, student=loggedStudent)
                        
                        subjectId = request.POST.get('id')
                        name = form.cleaned_data['name']
                        weight = form.cleaned_data['weight']
                        value = form.cleaned_data['value']

                        subjectSelected = get_object_or_404(Subject, pk=subjectId, period=periodSelected, student=loggedStudent)

                        newNote = Note(name=name, weight=weight, value=value, subject=subjectSelected, period=periodSelected)
                        newNote.save()
        return redirect('subject',periodId)

@login_required
def deleteNote(request, periodId):
        if(request.method == 'POST'):
                loggedStudent = getLoggedStudent(request)
                periodSelected = get_object_or_404(Period, pk=periodId, student=loggedStudent)

                noteId = request.POST.get('id_note')
                selectedSubjectId = request.POST.get('id_subject')

                selectedSubject = get_object_or_404(Subject, pk=selectedSubjectId, period=periodSelected, student=loggedStudent)

                noteSelected = get_object_or_404(Note, pk=noteId, subject=selectedSubject, period=periodSelected)
                noteSelected.delete()

        return redirect('subject',periodId)

@login_required
def editNote(request, periodId):
        if(request.method == 'POST'):
                loggedStudent = getLoggedStudent(request)
                periodSelected = get_object_or_404(Period, pk=periodId, student=loggedStudent)
                
                noteId = request.POST.get('id_note')
                subjectId = request.POST.get('id_subject')
                name = request.POST.get('name')
                weight = request.POST.get('weight')
                value = request.POST.get('value')

                selectedSubject = get_object_or_404(Subject, pk=subjectId, period=periodSelected, student=loggedStudent)

                selectedNote = get_object_or_404(Note, pk=noteId, subject=selectedSubject, period=periodSelected)

                selectedNote.name = name
                selectedNote.weight = int(weight)
                selectedNote.value = int(value)

                selectedNote.save()

        return redirect('subject',periodId)
        