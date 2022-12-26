from rest_framework import serializers
from django.contrib.auth.models import *
from apps.locations.models import *

class DepartmentSerializer(serializers.ModelSerializer):
    state_name = serializers.CharField(read_only=True)
    class Meta:
        model = Department
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(read_only=True)
    state_name = serializers.CharField(read_only=True)
    class Meta:
        model = City
        fields = '__all__'

    def validate_department(self, data):
        if data.state.name != 'active':
            raise serializers.ValidationError(('The department is invalid, please contact administrador.'), code='invalid')
        return data

class NeighborhoodSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(read_only=True)
    city_name = serializers.CharField(read_only=True)
    state_name = serializers.CharField(read_only=True)
    class Meta:
        model = Neighborhood
        fields = '__all__'
    
    def validate_city(self, data):
        if data.state.name != 'active':
            raise serializers.ValidationError(('The city is invalid, please contact administrador.'), code='invalid')
        return data

class PollingPlaceSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(read_only=True)
    city_name = serializers.CharField(read_only=True)
    neighborhood_name = serializers.CharField(read_only=True)
    state_name = serializers.CharField(read_only=True)
    class Meta:
        model = PollingPlace
        fields = '__all__'

    def validate_neighborhood(self, data):
        if data.state.name != 'active':
            raise serializers.ValidationError(('The neighborhood is invalid, please contact administrador.'), code='invalid')
        return data