from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Airplane(models.Model):
    name = models.CharField(max_length=100)
    business_seat_count = models.PositiveIntegerField(null=True, blank=True, default=0)
    economy_seat_count = models.PositiveIntegerField()
    seat_count_total = models.PositiveIntegerField(null=True, blank=True, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other fields below 
    
    def save(self, *args, **kwargs):
        self.seat_count_total = (self.business_seat_count or 0) + (self.economy_seat_count or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class TravelClass(models.Model):
    name = models.CharField(
        choices=(
            ('Business', 'Business'), 
            ('Economy', 'Economy')
        )
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    extra_fee = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class FlightSchedule(models.Model):
    plane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    from_location = models.CharField(
        max_length=100, 
        choices=(
            ('Port Harcourt', 'Port Harcourt'), 
            ('Abuja', 'Abuja'), 
            ('Lagos', 'Lagos'), 
            ('Owerri', 'Owerri'),
            ('Kano', 'Kano')
        )
    )
    to_location = models.CharField(
        max_length=100, 
        choices=(
            ('Port Harcourt', 'Port Harcourt'), 
            ('Abuja', 'Abuja'), 
            ('Lagos', 'Lagos'), 
            ('Owerri', 'Owerri'),
            ('Kano', 'Kano')
        )
    )
    select_travel_class = models.ManyToManyField(TravelClass)
    eta = models.CharField(
        max_length=50, 
        choices=(
            ('30m', '30m'), 
            ('45m', '45m'), 
            ('1h', '1h'), 
            ('1h 15m', '1h 15m'), 
            ('1h 30m', '1h 30m'), 
            ('2h', '2h')
        )
    )
    max_baggage_weight = models.PositiveIntegerField(default=20)
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class FlightBooking(models.Model):
    flight_schedule = models.ForeignKey(FlightSchedule, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    gender = models.CharField(
        max_length=20, 
        choices=(
            ('Male', 'Male'), 
            ('Female', 'Female')
        )
    )
    select_travel_class = models.ForeignKey(TravelClass, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    total_amount = models.PositiveIntegerField()
