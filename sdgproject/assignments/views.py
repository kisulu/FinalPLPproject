from django.shortcuts import render
from .models import AssignmentRequest

def assignment_list(request):
    assignments = AssignmentRequest.objects.all().order_by('-created_at')
    return render(request, "assignments/assignment_list.html", {"assignments": assignments})

