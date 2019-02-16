from django.contrib import admin
from .models import Note, Subject, Period

admin.site.register(Note)
admin.site.register(Subject)
admin.site.register(Period)