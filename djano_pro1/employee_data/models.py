from django.db import models

class EmployeeData(models.Model):
    emp_name = models.CharField(max_length=25)
    emp_salary = models.CharField(max_length=25)
    emp_id = models.CharField(max_length=25)

    