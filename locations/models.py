from django.db import models
from states.models import *

class Department(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class PollingPlace(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    coordinates_lat = models.CharField(max_length=100)
    coordinates_len = models.CharField(max_length=100)
    n_polling_station = models.IntegerField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
