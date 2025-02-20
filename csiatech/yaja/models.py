
from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class Monday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True)
    history = HistoricalRecords()


class Tuesday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True)
    history = HistoricalRecords()


class Wednesday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True)
    history = HistoricalRecords()


class Thursday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True)
    history = HistoricalRecords()


# Default schedules for users
class DefaultMonday(models.Model):
    student_id = models.CharField(max_length=10, null=True, blank=True)
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    history = HistoricalRecords()


class DefaultTuesday(models.Model):
    student_id = models.CharField(max_length=10, null=True, blank=True)
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    history = HistoricalRecords()


class DefaultWednesday(models.Model):
    student_id = models.CharField(max_length=10, null=True, blank=True)
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    history = HistoricalRecords()


class DefaultThursday(models.Model):
    student_id = models.CharField(max_length=10, null=True, blank=True)
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    history = HistoricalRecords()
