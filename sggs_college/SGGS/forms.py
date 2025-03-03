from django import forms
from .models import Attendance, Student, Subject

# Attendance form
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'subject', 'date', 'present']

# Student form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'branch', 'subjects', 'year_of_enrollment', 'gender', 'email']

# Subject form
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'branch']
