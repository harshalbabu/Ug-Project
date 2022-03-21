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
    flight = Flight_details.objects.get(trip_id=pk)
    context = {
        "f" : flight,
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
    code = request.POST['code']
    pn = request.POST['phone']
    em = request.POST['email']
    no = request.POST['number']
    seat = request.POST['seat']
    cost = request.POST['cost']
    for i in range(int(no)):
        i = i+1;
        f_name = request.POST['f_name'+str(i)]
        l_name = request.POST['l_name'+str(i)]
        g = request.POST['gender'+str(i)]
        print(code,pn,em,f_name,l_name,g,cost,sep="-")
        Booking.objects.create(
            passanger_id=m,
            trip_id=pk,
            f_name=f_name,
            l_name=l_name,
            g=g,
            code=code,
            pn=pn,
            email=em,
            seat=seat,
            cost=cost
        )
        m=m+1
    return render(request, "payment.html", context)