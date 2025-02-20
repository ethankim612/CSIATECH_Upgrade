# models.py
from django.db import models


class Reservation(models.Model):
    student1 = models.CharField(max_length=20, blank=True)
    student2 = models.CharField(max_length=20, blank=True)
    student3 = models.CharField(max_length=20, blank=True)
    student4 = models.CharField(max_length=20, blank=True)
    student5 = models.CharField(max_length=20, blank=True)
    student6 = models.CharField(max_length=20, blank=True)
    period1 = models.BooleanField(default=False)
    period2 = models.BooleanField(default=False)
    period3 = models.BooleanField(default=False)
    room_number = models.IntegerField()


class Room(models.Model):
    room_number = models.IntegerField()
    period1 = models.BooleanField(default=False)
    period2 = models.BooleanField(default=False)
    period3 = models.BooleanField(default=False)
  