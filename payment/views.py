import requests
import uuid
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from django.core.paginator import Paginator
from .models import Payment
from .filters import PaymentFilter
from booking.models import FlightBooking

User = get_user_model()

# generate reference
def generate_reference():
    return str(uuid.uuid4()).replace('-', '')[:12]

# initialize payment
def initialize_payment(request):
    booking_id = request.session.get('booking_id')

    if booking_id:
        checkout = FlightBooking.objects.get(id=booking_id)

        amount = int(checkout.total_amount) * 100 # convert to kobo
        email = checkout.email
        reference = generate_reference()

        headers = {
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}', 
            'Content-Type': 'application/json',
        }

        data = {
            'email':email, 'amount':amount, 'reference':reference, 
            'callback_url': request.build_absolute_uri(reverse('verify-payment', args=[reference])),
        }

        response = requests.post('https://api.paystack.co/transaction/initialize', json=data, headers=headers)

        response_data = response.json()

        if response_data.get('status'):
            Payment.objects.create(
                amount=amount/100, reference=reference, email=email
            )
            return redirect(response_data['data']['authorization_url'])
        else:
            messages.warning(request, 'Payment initialization failed. Please try again')
            return redirect('dashboard')
    else:
        messages.warning(request, 'Are you sure you used the check out page? Please try this again')
        return redirect('product-details')

# verify payment
def verify_payment(request, reference):
    headers = {
        'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}'
    }

    response = requests.get(f'https://api.paystack.co/transaction/verify/{reference}', headers=headers)

    response_data = response.json()

    try:
        payment = Payment.objects.get(reference=reference)
    except Payment.DoesNotExist:
        messages.warning(request, 'Payment not found')
        return redirect('dashboard')
    
    if response_data.get('status') and response_data.get('data', {}).get('status') == 'success':
        if not payment.verified:
            payment.verified = True
            payment.save()

            booking_id = request.session.get('booking_id')

            if booking_id:
                checkout = FlightBooking.objects.get(id=booking_id)
                checkout.is_verified = True
                checkout.save()
                send_mail(
                    'BOOKING CONFIRMATION AND ITINERY',
                    f'Hi {checkout.first_name}, Thank you for your flight booking. Your reservation has been received and confirmed. Please arrive at the airport at least 90 minutes before departure. We look forward to having you on board.',  # The body of the email
                    'noreply@email.com',
                    [checkout.email]
                )
                messages.success(request, 'Your payment was successful and your flight itinery has been sent to your mailbox.')
                return redirect('booking-success')
        
    messages.warning(request, 'Payment verification failed')
    return redirect('book-flight', checkout.flight_schedule.pk)



