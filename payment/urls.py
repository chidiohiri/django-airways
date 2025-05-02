from django.urls import path 
from . import views 

urlpatterns = [
    path('initialize-payment/', views.initialize_payment, name='initialize-payment'), 
    path('verify-payment/<str:reference>/', views.verify_payment, name='verify-payment'), 
]