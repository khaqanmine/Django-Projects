from django.db import models

class StudentInfo(models.Model):

    name = models.CharField(max_length=20)
    roll_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    father_name  = models.CharField(max_length=20)

# Create your models here.
