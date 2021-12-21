from django.db import models

class TeacherData(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    salary = models.IntegerField()

# Create your models here.
