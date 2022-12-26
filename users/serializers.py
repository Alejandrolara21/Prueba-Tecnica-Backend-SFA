from rest_framework import serializers
from django.contrib.auth.models import *
from users.models import *
from locations.models import *


class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'role_name',
            'role'            
        ]

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class UserLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]

class LeaderSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    document_type_name = serializers.CharField(read_only=True)
    class Meta:
        model = Leader
        fields = '__all__'


class VoterSerializer(serializers.ModelSerializer):
    document_type_name = serializers.CharField(read_only=True) 
    state_name = serializers.CharField(read_only=True)
    leader_name = serializers.CharField(read_only=True)
    polling_place_name = serializers.CharField(read_only=True)
    department_name = serializers.CharField(read_only=True)
    city_name = serializers.CharField(read_only=True)
    neighborhood_name = serializers.CharField(read_only=True)
    class Meta:
        model = Voter
        fields = '__all__'
        # fields = [
        #     'first_name',
        #     'last_name',
        #     'document_type',
        #     'document',
        #     'phone',
        #     'polling_station',
        #     'polling_place',
        #     'document_type_name',
        #     'state_name',
        #     'leader_name',
        #     'polling_place_name',
        #     'department_name',
        #     'city_name',
        #     'neighborhood_name'
        # ]
    
    def validate_phone(self, data):
        if len(data) != 10:
            raise serializers.ValidationError(('The phone is invalid, it has to have 10 digits.'), code='invalid')
        return data

    def validate(self, data):
        if(data['polling_place'].n_polling_station < data['polling_station']):
            raise serializers.ValidationError(('The polling station is invalid. The polling place has '+str(data['polling_place'].n_polling_station) +' polling stations.'), code='invalid')
        return data