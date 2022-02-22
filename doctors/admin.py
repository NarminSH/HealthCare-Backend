from django.contrib import admin
from doctors.models import WorkCategory, Doctor

# Register your models here.
@admin.register(WorkCategory)
class WorkCategoryAdmin(admin.ModelAdmin):
    display = 'title'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'field')

