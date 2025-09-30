# payments/models.py
import uuid
from django.db import models
from profiles.models import Profile
from sessions.models import TutoringSession

class Payment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]
    METHOD_CHOICES = [
        ("mpesa", "M-Pesa"),
        ("card", "Card"),
        ("bank_transfer", "Bank Transfer"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(TutoringSession, on_delete=models.CASCADE)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="payments_made")
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="payments_received")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default="KES")
    payment_method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
