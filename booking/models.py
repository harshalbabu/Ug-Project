from django.db import models

# Create your models here.
class Flight_details(models.Model):
    trip_id = models.IntegerField(primary_key=True)
    flight_no = models.IntegerField()
    flight_name = models.CharField(max_length=20)
    from_to = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    cost_e = models.IntegerField()
    cost_b = models.IntegerField()

class Booking(models.Model):
    passanger_id = models.AutoField(primary_key=True)
    trip_id = models.IntegerField()
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    g = models.CharField(max_length=1)
    code = models.IntegerField()
    pn = models.IntegerField()
    email = models.CharField(max_length=20)
    seat = models.CharField(max_length=1)
    cost = models.IntegerField()

