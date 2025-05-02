from django.urls import path
from .views import flight_schedule_list

urlpatterns = [
    path('flight-schedules/', flight_schedule_list, name='flight-schedule-list'),
]
