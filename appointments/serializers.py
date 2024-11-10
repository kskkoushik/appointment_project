# appointments/serializers.py
from rest_framework import serializers

class AppointmentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    dateTime = serializers.DateTimeField()
    comments = serializers.CharField(allow_blank=True, required=False)
    status = serializers.ChoiceField(choices=["pending", "confirmed", "canceled"], default="pending")
