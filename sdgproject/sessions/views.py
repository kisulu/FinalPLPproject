from django.shortcuts import render
from .models import TutoringSession

# Create your views here.

def session_list(request):
    sessions = TutoringSession.objects.all().order_by('-created_at')
    return render(request, "sessions/session_list.html", {"sessions": sessions})

