from os import name
from django.urls import path
from patients.api.views import (PatientsAPIView, PatientAPIView, PatientAppointmentsAPIView)

app_name = 'patients_api'

urlpatterns = [
    path('patients/', PatientsAPIView.as_view(), name='patients'),
    path('patients/<int:pk>', PatientAPIView.as_view(), name='patient'),
    path('patients/<int:pk>/appointments', PatientAppointmentsAPIView.as_view(), name='patient_appointments')
]