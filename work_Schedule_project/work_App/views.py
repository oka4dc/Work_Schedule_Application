from django.shortcuts import render
from .models import Staff, Staff_Grade

# Create your views here.
def index(request):
    staffs=Staff.objects.all()
    context={
        'staff':staffs
    }
    return render(request, 'Home.html', context)
