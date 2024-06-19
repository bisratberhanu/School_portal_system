from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal


class UserType(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        abstract = True


class Student(UserType):
    CGPA = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(Decimal('4.00')), MinValueValidator(Decimal('0.00'))])
    join_year = models.DateField(auto_now_add=True)


class Staff(UserType):
    office_number = models.PositiveSmallIntegerField()


class Admin(UserType):
    ROLE_CHOICES = [
        ('R', 'Register'),
        ('S', 'System Admin'),
    ]
    admin_role = models.CharField(max_length=1, choices=ROLE_CHOICES)


class Course(models.Model):
    name = models.CharField(max_length=200)
    credit_hour = models.PositiveSmallIntegerField(validators=[MaxValueValidator(35)])
    

class CourseRequirement(models.Model):
    courses = models.ManyToManyField(Course, related_name='required_courses')

