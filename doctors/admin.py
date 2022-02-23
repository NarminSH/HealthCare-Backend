from django.contrib import admin
from doctors.models import Appointment, WorkCategory, Doctor

# Register your models here.
@admin.register(WorkCategory)
class WorkCategoryAdmin(admin.ModelAdmin):
    display = 'title'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'field')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date')