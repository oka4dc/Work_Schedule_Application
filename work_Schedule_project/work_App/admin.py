from django.contrib import admin
from .models import Staff, Staff_Grade

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    Listdisplay=('FirstName', 'LastName', 'Gross_Salary')

class StaffGradeAdmin(admin.ModelAdmin):
    Listdisplay=('Position', 'Basic_Salary')

admin.site.register(Staff_Grade, StaffGradeAdmin)
admin.site.register(Staff, StaffAdmin)