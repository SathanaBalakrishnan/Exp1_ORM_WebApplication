from django.contrib import admin
from .models import employee,EmployeeAdmin
# Register your models here.
admin.site.register(employee,EmployeeAdmin)