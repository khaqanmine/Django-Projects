from django.contrib import admin
from .models import EmployeeData

@admin.register(EmployeeData)
class EmployeeDataAdmin(admin.ModelAdmin):
    list_display = ['emp_name', 'emp_salary', 'emp_id']
