from .models import *
from rest_framework import serializers


class ZahimarPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZahimarImagePrediction
        fields = ['image']

class ZahimargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZahimarImagePrediction
        fields = ['classes']