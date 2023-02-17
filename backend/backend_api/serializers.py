from rest_framework import serializers
from .models import * 


class TexileAppTestqtSerializer(serializers.ModelSerializer):
    class Meta:
        model = TexileAppTestqt
        fields = '__all__'

class TexileAppReleasedLotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TexileAppReleasedLots
        fields = '__all__'
