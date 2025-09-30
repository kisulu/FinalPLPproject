# sessions/models.py
import uuid
from django.db import models
from profiles.models import Profile
from subjects.models import Subject

class TutoringSession(models.Model):
    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    SESSION_TYPE_CHOICES = [
        ("homework_help", "Homework Help"),
        ("regular_tutoring", "Regular Tutoring"),
        ("exam_prep", "Exam Prep"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sessions_as_teacher")
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sessions_as_student")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration_hours = models.DecimalField(max_digits=5, decimal_places=2)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    session_type = models.CharField(max_length=20, choices=SESSION_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    meeting_link = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class TeacherAvailability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="availability")
    day_of_week = models.IntegerField()  # 0=Monday ... 6=Sunday
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

