from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)


class City(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class PollingPlace(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    coordinates_lat = models.CharField(max_length=100, blank=True, null=True)
    coordinates_len = models.CharField(max_length=100, blank=True, null=True)
    n_polling_station = models.IntegerField(null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
