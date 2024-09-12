from django.db import models



class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Professor model
class Professor(models.Model):
    professor = models.CharField(max_length=60)
    department = models.ForeignKey(Faculty,related_name='professor' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.professor} - {self.title}"

# Student model
class Student(models.Model):
    user = models.CharField(max_length=60)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.department.name}"

# Course model
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

# Classroom model
class Classroom(models.Model):
    room_number = models.CharField(max_length=10)
    building = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.building} {self.room_number}"

# Schedule model
class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])

    def __str__(self):
        return f"{self.course.name} in {self.classroom} on {self.day_of_week}"

# Enrollment model
class Enrollment(models.Model):
    student = models.ForeignKey(Student,related_name='student',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,related_name='course',on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    grade = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.course.name}"
