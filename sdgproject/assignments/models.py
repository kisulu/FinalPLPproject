# assignments/models.py
import uuid
from django.db import models
from profiles.models import Profile
from subjects.models import Subject

class AssignmentRequest(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("assigned", "Assigned"),
        ("completed", "Completed"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="assignment_requests")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    budget_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    assigned_teacher = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_assignments")
    attachment_urls = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
