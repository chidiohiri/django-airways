from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.flight_schedules, name='flight-schedules'), 
    path('book-flight/<int:pk>/', views.book_flight, name='book-flight'), 
    path('booking-success/', views.booking_success, name='booking-success')
]