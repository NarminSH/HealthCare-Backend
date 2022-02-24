from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView
)
from django.http.response import JsonResponse
from doctors.api.serializers import (
    DoctorListSerializer,
    DoctorSerializer,
    WorkCategorySerializer,
    AppointmentListSerializer,
    AppointmentSerializer
)

from doctors.models import Doctor, WorkCategory, Appointment


class DoctorsAPIView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DoctorListSerializer
        return super(DoctorsAPIView, self).get_serializer_class()


class DoctorAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    lookup_url_kwarg = "pk"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DoctorListSerializer
        return super(DoctorAPIView, self).get_serializer_class()


class CategoriesAPIView(ListAPIView):
    queryset = WorkCategory.objects.all()
    serializer_class = WorkCategorySerializer


class DoctorAppointmentsAPIView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer

    def get(self, *args, **kwargs):
        current_doctor = Doctor.objects.filter(id=kwargs.get("pk")).first()
        appointments = Appointment.objects.filter(doctor=current_doctor)
        if not appointments:
            return JsonResponse(data=[], status=200, safe=False)
        print(appointments)
        serializer = AppointmentListSerializer(
            appointments, many=True, context={"request": self.request}
        )
        return JsonResponse(data=serializer.data, safe=False)


class AppointmentsAPIView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def post(self, *args, **kwargs):
        appointment_data = self.request.data
        serializer = AppointmentSerializer(data=appointment_data, context={
                                            'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)
