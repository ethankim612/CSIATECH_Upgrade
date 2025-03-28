from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class Monday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True, unique=True)
    history = HistoricalRecords()


class Tuesday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True, unique=True)
    history = HistoricalRecords()


class Wednesday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True, unique=True)
    history = HistoricalRecords()


class Thursday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True, unique=True)
    history = HistoricalRecords()

