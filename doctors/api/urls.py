from django.urls import path
from doctors.api.views import (
    CommentsAPIView,
    DoctorsAPIView,
    DoctorAPIView,
    DoctorAppointmentsAPIView,
    DoctorCommentsAPIView,
    AppointmentsAPIView,
    AppointmentAPIView
)

app_name = "doctors_api"

urlpatterns = [
    path("doctors/", DoctorsAPIView.as_view(), name="doctors"),
    path("doctors/<int:pk>", DoctorAPIView.as_view(), name="doctor"),
    path(
        "doctors/<int:pk>/appointments",
        DoctorAppointmentsAPIView.as_view(),
        name="doctor_appointments",
    ),
    path("appointments/", AppointmentsAPIView.as_view(), name="appointments"),
    path("appointments/<int:pk>", AppointmentAPIView.as_view(), name="appointment"),
    path("comments/", CommentsAPIView.as_view(), name="comments"),
    path(
        "doctors/<int:pk>/comments",
        DoctorCommentsAPIView.as_view(),
        name="doctor_comments",
    ),
]
