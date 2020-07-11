from rest_framework import serializers
# own app
from market.models import Market


class MarketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Market
        fields = ['url', 'name']
