from django.urls import path
from .views import booking_details

app_name = "booking"

urlpatterns = [
    path('', booking_details),
]