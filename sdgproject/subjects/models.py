# subjects/models.py
import uuid
from django.db import models
from profiles.models import Profile  # cross-app import

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TeacherSubject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="teacher_subjects")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="teacher_subjects")
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    experience_years = models.IntegerField()

    def __str__(self):
        return f"{self.teacher} - {self.subject}"
