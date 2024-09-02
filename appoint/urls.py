from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("index",views.index,name="Index"),
    path("about",views.about,name="About"),
    path("appointment",views.appointment,name="Appointment"),
    path("bookAppointment",views.book_appointment,name="Appointment"),
    path("patientIndex",views.patient,name="Patient"),
    path("DoctorIndex",views.doctor,name="doctor"),
    path("delete",views.delete,name="delete")
]