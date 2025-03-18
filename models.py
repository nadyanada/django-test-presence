from django.db import models
from django.utils import timezone

class AttendanceShortTerm(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    timestamp = models.DateTimeField(default=timezone.now)
    processed = models.BooleanField(default=False)

    class Meta:
        db_table = 'attendance_default'

class AttendanceLongTerm(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    timestamp = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        db_table = 'attendance_longterm'