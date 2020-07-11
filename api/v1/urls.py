from django.conf.urls import url, include
from rest_framework import routers

# import api.v1.serializers as serializers
from api.v1.viewsets import (
    user_viewset,
    market_viewset,
    currency_viewset,
    key_viewset,
    position_viewset,
    transaction_viewset,
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', user_viewset.UserViewSet)
router.register(r'markets', market_viewset.MarketViewset)
router.register(r'currencies', currency_viewset.CurrencyViewset)
router.register(r'keys', key_viewset.KeyViewset)
router.register(r'positions', position_viewset.PositionViewset)
router.register(r'transactions', transaction_viewset.TransactionViewset)


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
