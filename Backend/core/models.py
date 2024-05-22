from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('A', 'Admin')
    ]
    username = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False, unique=True)
    
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    old_password = models.CharField(max_length=20)
    


class InitialUser(models.Model):
    ROLE_CHOICES = [
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('A', 'Admin')
    ]
    username = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    password = models.CharField(max_length=20)
