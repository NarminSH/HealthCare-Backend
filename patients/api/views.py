from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from django.http.response import JsonResponse
from doctors.api.serializers import AppointmentListSerializer
from patients.api.serializers import PatientSerializer
from patients.models import Patient
from doctors.models import Appointment


class PatientsAPIView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientAppointmentsAPIView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer

    def get(self, *args, **kwargs):
        current_patient = Patient.objects.filter(id=kwargs.get("pk")).first()
        appointments = Appointment.objects.filter(patient=current_patient)
        if not appointments:
            return JsonResponse(data=[], status=200, safe=False)
        serializer = AppointmentListSerializer(
            appointments, many=True, context={"request": self.request}
        )
        return JsonResponse(data=serializer.data, safe=False)
