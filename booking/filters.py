import django_filters
from .models import FlightSchedule

class FlightScheduleFilter(django_filters.FilterSet):
    class Meta:
        model = FlightSchedule
        fields = ['departure_date', 'from_location', 'to_location'] 