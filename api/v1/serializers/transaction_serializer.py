from rest_framework import serializers
# own app
from market.models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['url', 'market', 'date', 'action', 'from_currency', 'to_currency', 'from_amount', 'to_amount']
