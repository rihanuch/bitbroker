from rest_framework import serializers
# own app
from market.models import Key


class KeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Key
        fields = ['url', 'market', 'api_key', 'api_secret']