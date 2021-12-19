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
    e_n = models.BooleanField(default=False)
    n_t = models.BooleanField(default=False)
    t_e = models.BooleanField(default=False)
    e_t = models.BooleanField(default=False)
    t_o = models.BooleanField(default=False)
    o_t = models.BooleanField(default=False)
    t_th = models.BooleanField(default=False)