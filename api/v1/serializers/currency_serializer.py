from rest_framework import serializers
# own app
from market.models import Currency

# Serializers define the API representation.
class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ['url', 'name', 'symbol']