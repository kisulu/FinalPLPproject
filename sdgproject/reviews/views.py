from django.shortcuts import render
from .models import Review

def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, "reviews/review_list.html", {"reviews": reviews})
