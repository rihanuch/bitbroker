from rest_framework import viewsets
# permissions
from rest_framework import permissions
from api.permissions import (
    read_only
)
from api.v1.serializers.currency_serializer import CurrencySerializer, Currency


class CurrencyViewset(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [
        permissions.IsAdminUser | read_only.ReadOnly
    ]
