from django.urls import path
from doctors.api.views import (DoctorsAPIView, DoctorAPIView, DoctorAppointmentsAPIView)

app_name = 'doctors_api'

urlpatterns = [
    path('doctors/', DoctorsAPIView.as_view(), name='doctors'),
    path('doctors/<int:pk>', DoctorAPIView.as_view(), name='doctor'),
    path('doctors/<int:pk>/appointments', DoctorAppointmentsAPIView.as_view(), name='doctor_appointments'),
    # path('appointments/', )
]