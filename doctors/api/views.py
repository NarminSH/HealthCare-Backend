from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from django.http.response import JsonResponse
from doctors.api.serializers import (
    CommentListSerializer,
    CommentSerializer,
    DoctorListSerializer,
    DoctorSerializer,
    WorkCategorySerializer,
    AppointmentListSerializer,
    AppointmentSerializer,
)

from doctors.models import Comment, Doctor, WorkCategory, Appointment


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


class AppointmentsAPIView(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AppointmentListSerializer
        return super(AppointmentsAPIView, self).get_serializer_class()

    def post(self, *args, **kwargs):
        appointment_data = self.request.data
        serializer = AppointmentSerializer(
            data=appointment_data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)



class AppointmentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    lookup_url_kwarg = "pk"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AppointmentListSerializer
        return super(AppointmentAPIView, self).get_serializer_class()



class CommentsAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return super(CommentsAPIView, self).get_serializer_class()

    def post(self, *args, **kwargs):
        comment_data = self.request.data
        serializer = CommentSerializer(
            data=comment_data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(data=serializer.data, safe=False, status=201)