from django.db import models
from django.contrib import admin
# Create your models here.
class employee(models.Model):
    employee_name = models.CharField(max_length=20, help_text="Enter employee Name")
    age = models.IntegerField(help_text="Enter age between 18 to 22")
    dob = models.DateField()
    employee_id = models.IntegerField(help_text="Enter the employee ID")

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name','age','dob','employee_id'] 