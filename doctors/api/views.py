from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, 
                                        CreateAPIView)
from django.http.response import JsonResponse
from doctors.api.serializers import (AppointmentSerializer, DoctorListSerializer, DoctorSerializer, 
                            WorkCategorySerializer, AppointmentListSerializer)

from doctors.models import Doctor, WorkCategory, Appointment


class DoctorsAPIView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DoctorListSerializer
        return super(DoctorsAPIView, self).get_serializer_class()



class DoctorAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    lookup_url_kwarg = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DoctorListSerializer
        return super(DoctorAPIView, self).get_serializer_class()


class CategoriesAPIView(ListAPIView):
    queryset = WorkCategory.objects.all()
    serializer_class = WorkCategorySerializer

    

class DoctorAppointmentsAPIView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer

    def get(self, *args, **kwargs):
            appointments = Appointment.objects.filter(patient=kwargs.get('pk'))
            if not appointments:
                return JsonResponse (data=[], status=200, safe=False)
            serializer = AppointmentListSerializer(
                appointments, context={'request': self.request})
            return JsonResponse(data=serializer.data, safe=False)


# class Appointments(CreateAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

#     def create(self, *args, **kwargs)

    