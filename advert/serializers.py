from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from advert.models import Advertiser

class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ('name', 'address', 'credit_limit')