from django.contrib import admin
from .models import Airplane, TravelClass, FlightSchedule

admin.site.register(Airplane)
admin.site.register(TravelClass)
admin.site.register(FlightSchedule)
