from django import forms
from .models import FlightBooking, TravelClass

class FlightBookingForm(forms.ModelForm):
    select_travel_class = forms.ModelChoiceField(queryset=TravelClass.objects.none())
    class Meta:
        model = FlightBooking
        exclude = ('flight_schedule', 'timestamp', 'unique_id', 'is_verified', 'total_amount')

    def __init__(self, *args, **kwargs):
        flight_schedule = kwargs.pop('flight_schedule', None)
        super().__init__(*args, **kwargs)

        if flight_schedule:
            self.fields['select_travel_class'].queryset = flight_schedule.select_travel_class.all()
        else:
            self.fields['select_travel_class'].queryset = TravelClass.objects.none()