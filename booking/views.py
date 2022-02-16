from django.shortcuts import render
from .models import Flight_details
# Create your views here.
def booking_details(request):
    details = Flight_details.objects.all()
    context = {
        "data" : details
    }
    return render(request, "flight_details.html", context)


def flight_detail(request, pk):
    print(pk)
    flight = Flight_details.objects.get(id=pk)
    context = {
        "f" : flight
    }
    return render(request, "flight.html", context)