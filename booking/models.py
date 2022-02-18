from django.db import models

# Create your models here.
class Flight_details(models.Model):
    trip_id = models.IntegerField(primary_key=True)
    flight_no = models.IntegerField()
    flight_name = models.CharField(max_length=20)
    from_to = models.CharField(max_length=20)
    to = models.CharField(max_length=20)

class Booking(models.Model):
    passanger_id = models.AutoField(primary_key=True)
    trip_id = models.IntegerField()
    name = models.CharField(max_length=20)

