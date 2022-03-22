from django.urls import path
from .views import booking_details, flight_detail, passanger_details, payment

app_name = "booking"

urlpatterns = [
    path('', booking_details),
    path('<int:pk>/', flight_detail),
    path('<int:pk>/book/', passanger_details),
    path('<int:pk>/pay/', payment),
]