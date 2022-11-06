from django.shortcuts import render
from work_App.models import Staff, Staff_Grade
# Create your views here.
def index(request):
    staff=Staff.objects.filter()
    context={
        'staff':staff
    }
    return render(request, 'Home.html', context)