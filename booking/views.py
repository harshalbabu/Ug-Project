from django.shortcuts import render
from django.db.models import Max
from .models import Flight_details
from .models import Booking
from .forms import PassangerForm

# Create your views here.
def booking_details(request):
    details = Flight_details.objects.all()
    context = {
        "data" : details
    }
    return render(request, "flight_details.html", context)


def flight_detail(request, pk):
    flight = Flight_details.objects.get(trip_id=pk)
    context = {
        "f" : flight
    }
    return render(request, "flight.html", context)

def passanger_details(request, pk):
    form = PassangerForm()
    if request.method == "POST":
        print("recived post request")
        form = PassangerForm(request.POST)
        if form.is_valid():
            print(request.POST['name'])
            context = {
                "pk" : pk, 
                "passanger" : form
            }
            return render(request, "passanger_v.html", context)

    context = {
        "passanger" : PassangerForm(),
        "pk" : pk
    }
    return render(request, "passanger.html", context)

def payment(request, pk):
    context = {
        "pk" : pk
    }
    m = Booking.objects.aggregate(Max('passanger_id'))['passanger_id__max']
    if m is None:
        m = 0
    m = m + 1
    name = request.POST['name']
    print("paymeent - " + request.POST['name'], m)
    Booking.objects.create(
        passanger_id=m,
        trip_id=pk,
        name=request.POST['name']
    )
    return render(request, "payment.html", context)