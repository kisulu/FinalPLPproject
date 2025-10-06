from django.shortcuts import render
from .models import Payment

# Create your views here.
def payment_list(request):
    payments = Payment.objects.all().order_by('-created_at')
    return render(request, "payments/payment_list.html", {"payments": payments})
