from rest_framework import serializers
from patients.models import Patient



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id',
            'first_name',
            'surname',
            'phone_number',
            'location',
            'created_at',
            'updated_at',
        )