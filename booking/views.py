from django.shortcuts import render
import datetime
from django.db.models import Max
from .models import Flight_details
from .models import Booking
from .forms import PassangerForm
import math
import json
from datetime import timedelta
# Create your views here.
def booking_details(request):
    details = Flight_details.objects.order_by('from_time')
    f=open("list.json","r")
    r = json.load(f)[0]
    f.close()
    t = []
    f_time = []
    data = []
    for i in range(len(details)):
        if details[i].to == "CCJ":
            t =  False
        else:
            t = True
        f_pl = ""
        l_pl = ""
        for j in r:
            if j[0]== details[i].from_to:
                f_pl = j[1]
            if j[0]== details[i].to:
                l_pl = j[1]
        if details[i].cancellation==1:
            c = True
        else:
            c = False
        delay = list(range(4))
        if details[i].delay==0:
            isdelay = False
        else:
            isdelay = True
            dddd = timedelta(minutes=details[i].delay)
            ft = details[i].from_time + dddd
            delay[0] = ft.strftime("%I:%M %p")
            delay[1] = ft.strftime("%d %b")
            ft = details[i].to_time + dddd
            delay[2] = ft.strftime("%I:%M %p")
            delay[3] = ft.strftime("%d %b")
            

        ft = details[i].from_time.strftime("%I:%M %p")
        tt = details[i].to_time.strftime("%I:%M %p")
        fd = details[i].from_time.strftime("%d %b")
        td = details[i].to_time.strftime("%d %b")
        d = details[i].to_time - details[i].from_time
        d = divmod(math.ceil(divmod(d.total_seconds(), 60)[0])+1,60)
        if isdelay:
            (delay, (ft,fd,tt,td)) = ((ft,fd,tt,td), delay) 
        data.append((t, ft, tt, fd, td, f'{d[0]}h {d[1]}m', f_pl, l_pl, c, isdelay, delay[0],delay[1],delay[2],delay[3], details[i]))
    print(t,f_time)
    context = {
        "data" : data,
    }
    return render(request, "flight_details.html", context)

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
        m = 1000
    m = m + 1
    print(m)
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