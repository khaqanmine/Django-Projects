from django.db import models

class ContactFormModel(models.Model):
    
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=10)