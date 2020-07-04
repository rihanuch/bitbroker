from django.db import models
from django.conf import settings
from market.model.market import Market
from market.model.currency import Currency


class Transaction(models.Model):

    class Action(models.TextChoices):
        BUY = 'BUY', 'Buy'
        SELL = 'SELL', 'Sell'

    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    action = models.CharField(max_length=4, choices=Action.choices, default=Action.BUY)

    # if you want to buy 1 BTC at 7_500_000 CLP
    # then from_currency=CLP, from_amount=7_500_000
    # and  to_currency=BTC, to_amount=1
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='transactions_from')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='transactions_to')
    
    from_amount = models.FloatField()
    to_amount = models.FloatField()

    def ratio(self):
        """
        Ratio is from_amount/to_amount
        
        For example:
        if 1 BTC = 7_500_000 CLP, the ratio when buying BTC from CLP
        is 7_500_000 / 1
        """
        return self.from_amount / self.to_amount

    def inverted_ratio(self):
        """
        Returns inverted ratio
        For example:
        if 1 BTC = 7_500_000 CLP, the ratio when buying BTC from CLP
        is 1 / 7_500_000
        """
        return 1 / self.ratio()

    def __str__(self):
        return f'{self.market}[{self.date}]: {self.ratio()}({self.from_currency}/{self.to_currency})'