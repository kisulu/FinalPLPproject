# reviews/models.py
import uuid
from django.db import models
from profiles.models import Profile
from sessions.models import TutoringSession

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="reviews")
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="given_reviews")
    session = models.ForeignKey(TutoringSession, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

