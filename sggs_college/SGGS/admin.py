from django.contrib import admin
from .models import Branch, Subject, Faculty, Student, Attendance

# Register your models here.
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Attendance)
