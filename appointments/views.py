from django.shortcuts import render

# Create your views here.
# appointments/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppointmentSerializer
from django.conf import settings
from bson import ObjectId
from appointment_project.mongodb import db

 # MongoDB database instance

# Create Appointment
class AppointmentCreateView(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            appointment = serializer.data
            appointment['status'] = "pending"
            db.appointments.insert_one(appointment)
            return Response({"message": "Appointment created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List All Appointments
class AppointmentListView(APIView):
    def get(self, request):
        appointments = list(db.appointments.find())
        for appointment in appointments:
            appointment['_id'] = str(appointment['_id'])
        return Response(appointments, status=status.HTTP_200_OK)

# Update Appointment Status
class AppointmentUpdateView(APIView):
    def patch(self, request, appointment_id):
        status_update = request.data.get("status")
        if status_update not in ["pending", "confirmed", "canceled"]:
            return Response({"error": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)

        result = db.appointments.update_one(
            {"_id": ObjectId(appointment_id)},
            {"$set": {"status": status_update}}
        )

        if result.matched_count == 0:
            return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Status updated successfully."}, status=status.HTTP_200_OK)
