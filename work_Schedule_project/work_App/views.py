from django.shortcuts import render
from .models import Staff, Staff_Grade

# Create your views here.
def index(request):
    staff=Staff.objects.all()
    context={
        'staff':staff
    }
    return render(request, 'Home.html', context)
