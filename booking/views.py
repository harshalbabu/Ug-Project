from django.shortcuts import render
from .models import Flight_details
from .forms import PassangerForm

# Create your views here.
def booking_details(request):
    details = Flight_details.objects.all()
    context = {
        "data" : details
    }
    return render(request, "flight_details.html", context)


def flight_detail(request, pk):
    flight = Flight_details.objects.get(id=pk)
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
                "pk" : pk
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
    return render(request, "payment.html", context)