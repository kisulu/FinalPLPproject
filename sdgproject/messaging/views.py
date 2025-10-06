from django.shortcuts import render
from .models import Message

def message_list(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, "messaging/message_list.html", {"messages": messages})

