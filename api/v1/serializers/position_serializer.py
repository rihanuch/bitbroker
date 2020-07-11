from rest_framework import serializers
# own app
from market.models import Position


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['url', 'market', 'transaction_buy', 'transaction_sell', 'desired_return']
