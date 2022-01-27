from django.db import models

# Create your models here.
class Flight_details(models.Model):
    flight_no = models.IntegerField()
    flight_name = models.CharField(max_length=20)
    travel_id = models.IntegerField()
    from_to = models.CharField(max_length=20)
    to = models.CharField(max_length=20)

class Booking(models.Model):
    trip_id = models.ForeignKey(Flight_details, on_delete=models.SET_NULL, null=True)
    travel_id = models.IntegerField()
    name = models.CharField(max_length=20)

