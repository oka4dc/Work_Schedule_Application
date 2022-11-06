from django.db import models

# Create your models here.

class Staff_Grade(models.Model):
    Position=models.CharField(max_length=100)
    Basic_Salary=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.Position


class Staff(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Email=models.EmailField()
    Hours_work=models.PositiveIntegerField(default=0)
    Gross_Salary=models.PositiveIntegerField(default=0)
    Staff_Grade_Status=models.ForeignKey(Staff_Grade, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        self.Gross_Salary=(self.Hours_work * self.Staff_Grade_Status.Basic_Salary)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.FirstName