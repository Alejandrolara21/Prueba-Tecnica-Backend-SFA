from rest_framework import serializers
from django.contrib.auth.models import *
from states.models import *

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'