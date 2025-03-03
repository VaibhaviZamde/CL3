from django.db import models

# Branch Model
class Branch(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.name

# Subject Model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    branch = models.ForeignKey(Branch, related_name='subjects', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} ({self.code})"

# Faculty Model
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10, unique=True)
    branch = models.ForeignKey(Branch, related_name='faculties', on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='faculties')
    
    def __str__(self):
        return self.name

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=15, unique=True)
    branch = models.ForeignKey(Branch, related_name='students', on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='students')
    year_of_enrollment = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name  # Return student's name here instead of incorrectly accessing self.student.name

# Attendance Model
class Attendance(models.Model):
    student = models.ForeignKey('Student', related_name='attendance', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', related_name='attendance', on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.date} : {'Present' if self.present else 'Absent'}"
