from django.shortcuts import render
from .models import Profile

# Create your views here.
def teacher_list(request):
    teachers = Profile.objects.filter(user_type="teacher")
    return render(request, "profiles/teacher_list.html", {"teachers": teachers})
