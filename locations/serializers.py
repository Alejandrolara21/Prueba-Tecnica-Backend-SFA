from rest_framework import serializers
from django.contrib.auth.models import *
from locations.models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(read_only=True)
    class Meta:
        model = City
        fields = '__all__'

class NeighborhoodSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(read_only=True)
    city_name = serializers.CharField(read_only=True)
    class Meta:
        model = Neighborhood
        fields = '__all__'

class PollingPlaceSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(read_only=True)
    city_name = serializers.CharField(read_only=True)
    neighborhood_name = serializers.CharField(read_only=True)
    class Meta:
        model = PollingPlace
        fields = '__all__'