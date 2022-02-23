from django.db import models
from patients.models import Patient

# Create your models here.

class WorkCategory(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'WorkCategories'
    
    def __str__(self):
        return self.title



class Doctor(models.Model):
    #relations
    field = models.ForeignKey(WorkCategory, on_delete=models.CASCADE,
                db_index=True, related_name='doctors')
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=60)
    location = models.CharField(max_length=250, null=True)
    clinic = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.first_name

    


class Appointment(models.Model):
    #relations
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, 
                        db_index=True, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, 
                        db_index=True, related_name='appointments', null=True)
                        
    date = models.CharField(max_length=50, null=True)

    #moderations
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.doctor.first_name