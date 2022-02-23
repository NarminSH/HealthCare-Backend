from rest_framework import serializers
from doctors.models import Appointment, Doctor, WorkCategory
from patients.api.serializers import PatientSerializer


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            "id",
            "first_name",
            "surname",
            "location",
            "clinic",
            "created_at",
            "updated_at",
            "field",
        )


class WorkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkCategory
        fields = ("title", "created_at")


class DoctorListSerializer(DoctorSerializer):
    field = WorkCategorySerializer()


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("patient", "doctor", "date", "created_at", "updated_at")


class AppointmentListSerializer(AppointmentSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()
