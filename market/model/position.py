# python modules
import datetime
# django modules
from django.db import models
from django.conf import settings
# custom models
from market.model.market import Market
from market.model.transaction import Transaction


class PositionManager(models.Manager):
    pass


class Position(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='positions')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='positions')

    transaction_buy = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='positions_buy')
    transaction_sell = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='positions_sell', blank=True, null=True)

    desired_return = models.FloatField()

    objects = PositionManager()

    @property
    def closed(self):
        return self.transaction_sell is not None

    def return_rate(self):
        if not closed:
            return 0
        return self.transaction_sell.inverted_ratio() / self.transaction_buy.ration()

    def position_hold_time(self):
        if not closed:
            return datetime.datetime.now() - self.transaction_buy.date
        return self.transaction_sell.date - self.transaction_buy.date