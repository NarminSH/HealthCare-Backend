from django.db import models


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.first_name