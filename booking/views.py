import string
import random
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Airplane, TravelClass, FlightSchedule, FlightBooking
from .form import FlightBookingForm
from .filters import FlightScheduleFilter

# Show all Flight Schedules (Home page)
def flight_schedules(request):
    fs = FlightSchedule.objects.all()

    # apply filter 
    fs_filter = FlightScheduleFilter(request.GET, queryset=fs)
    filtered_fs = fs_filter.qs

    # pagination
    paginator = Paginator(filtered_fs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'fs':page_obj, 'filter':fs_filter}
    return render(request, 'booking/flight_schedules.html', context)

def generate_unique_id_for_today():
    charset = string.ascii_uppercase + string.digits
    today = timezone.now().date()

    while True:
        code = ''.join(random.choices(charset, k=6))
        exists = FlightBooking.objects.filter(unique_id=code, timestamp__date=today).exists()
        if not exists:
            return code

def book_flight(request, pk):
    flight_schedule = FlightSchedule.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = FlightBookingForm(request.POST, flight_schedule=flight_schedule)
        if form.is_valid():
            var = form.save(commit=False)
            var.flight_schedule = flight_schedule

            # Generate unique ID per day
            var.unique_id = generate_unique_id_for_today()

            if var.select_travel_class.name == 'Business': 
                var.total_amount = var.flight_schedule.amount + var.select_travel_class.extra_fee
            else:
                var.total_amount = var.flight_schedule.amount

            var.save()

            request.session['booking_id'] = var.id
            return redirect('initialize-payment')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
    else:
        form = FlightBookingForm(flight_schedule=flight_schedule)  

    context = {'form': form, 'flight_schedule': flight_schedule, 'business_extra_fee': TravelClass.objects.filter(name='Business').first().extra_fee}
    return render(request, 'booking/book_flight.html', context)


def booking_success(request):
    booking_id = request.session.get('booking_id')

    if booking_id:
        checkout = FlightBooking.objects.get(id=booking_id)
        context = {'checkout':checkout}
        return render(request, 'booking/booking_success.html', context)
    else:
        return redirect('flight-schedules')