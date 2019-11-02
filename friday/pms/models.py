# standard libray
from datetime import datetime

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    admission_number = models.IntegerField(
        help_text="Admission number as 6 digits(8292/17=829217)"
    )
    name = models.CharField(
        max_length=200
    )
    batch = models.CharField(
        max_length=10,
        help_text="Student's class"
    )
    year = models.PositiveSmallIntegerField(
        default=datetime.now().year
    )
