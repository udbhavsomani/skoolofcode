from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class AvailableTiming(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data = models.JSONField(default=dict)