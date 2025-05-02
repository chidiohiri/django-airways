from rest_framework import serializers
from booking.models import FlightSchedule, TravelClass, Airplane

class TravelClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelClass
        fields = ['id', 'name', 'extra_fee']  # adjust fields as needed

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['id', 'name']

class FlightScheduleSerializer(serializers.ModelSerializer):
    select_travel_class = TravelClassSerializer(many=True, read_only=True)
    plane = AirplaneSerializer(read_only=True)

    class Meta:
        model = FlightSchedule
        fields = '__all__'
