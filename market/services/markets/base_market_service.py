from abc import ABC, abstractmethod

class BaseMarketService(ABC):

    url = ''

    def __init__(self, user, market, auth=None):
        self.user = user
        self.market = market
        self.auth = auth
        super().__init__()

    @abstractmethod
    def generate_auth(self, *args, **kwargs):
        pass