from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from SGGS.models import Attendance, Student, Subject
from SGGS.forms import AttendanceForm, StudentForm, SubjectForm

# View for showing attendance
def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'SGGS/attendance_list.html', {'attendances': attendances})

# View for adding attendance
def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')  # Redirect to attendance list after saving
    else:
        form = AttendanceForm()
    return render(request, 'SGGS/add_attendance.html', {'form': form})

# View for showing all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'SGGS/student_list.html', {'students': students})

# View for adding a new student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list after saving
    else:
        form = StudentForm()
    return render(request, 'SGGS/add_student.html', {'form': form})

# View for showing all subjects
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'SGGS/subject_list.html', {'subjects': subjects})

# View for adding a new subject
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')  # Redirect to subject list after saving
    else:
        form = SubjectForm()
    return render(request, 'SGGS/add_subject.html', {'form': form})

def index(request):
    return render(request, 'index.html')