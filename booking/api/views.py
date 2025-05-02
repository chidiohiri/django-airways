from rest_framework.decorators import api_view
from rest_framework.response import Response
from booking.models import FlightSchedule
from .serializers import FlightScheduleSerializer

@api_view(['GET'])
def flight_schedule_list(request):
    flights = FlightSchedule.objects.all()
    serializer = FlightScheduleSerializer(flights, many=True)
    return Response(serializer.data)
