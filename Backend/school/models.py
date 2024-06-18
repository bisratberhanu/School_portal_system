from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal


class UserType(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        abstract = True

class Enrollment(models.Model):
    GRADE_CHOICES = [
        ('A', 'Excellent'),
        ('B', 'Very Good'),
        ('C', "Good"),
        ('D', 'Pass'),
        ('F', 'Fail'),
    ]
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)

class Course(models.Model):
    name = models.CharField(max_length=200)
    credit_hour = models.PositiveSmallIntegerField(validators=[MaxValueValidator(35)])
    enrollment = models.OneToOneField(Enrollment, on_delete=models.PROTECT, related_name="courses", primary_key=True)

class Department(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="departments")

class Program(models.Model):
    name = models.CharField(max_length=50)
    department = models.OneToOneField(Department, on_delete=models.CASCADE, primary_key=True)

class Student(UserType):
    CGPA = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(Decimal('4.00')), MinValueValidator(Decimal('0.00'))])
    join_year = models.DateField(auto_now_add=True)
    programs = models.ForeignKey(Program, on_delete=models.PROTECT)
    enrollment = models.ManyToManyField(Enrollment, on_delete=models.PROTECT)

class Staff(UserType):
    office_number = models.PositiveSmallIntegerField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="staff_department")
    enrollment = models.ForeignKey(Enrollment, on_delete=models.PROTECT)

class Admin(UserType):
    ROLE_CHOICES = [
        ('R', 'Register'),
        ('S', 'System Admin'),
    ]
    admin_role = models.CharField(max_length=1, choices=ROLE_CHOICES)

class Registrations(models.Model):
    SEMESTER_CHOICES = [
        ('1', 'First Semester'),
        ('2', 'Second Semester'),
    ]
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
    ]
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

class CourseRequirement(models.Model):
    courses = models.ManyToManyField(Course, related_name='required_courses')