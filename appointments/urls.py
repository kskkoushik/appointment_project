# appointments/urls.py
from django.urls import path
from .views import AppointmentCreateView, AppointmentListView, AppointmentUpdateView

urlpatterns = [
    path('appointments/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointments/list/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/<str:appointment_id>/', AppointmentUpdateView.as_view(), name='appointment-update'),
]
