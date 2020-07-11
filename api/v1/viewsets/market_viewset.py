from rest_framework import viewsets
# permissions
from rest_framework import permissions
from api.permissions import (
    read_only
)
from api.v1.serializers.market_serializer import MarketSerializer, Market


class MarketViewset(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [
        permissions.IsAdminUser | read_only.ReadOnly
    ]
