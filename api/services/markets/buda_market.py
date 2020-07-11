import base64
import hmac
import time
import requests.auth
# own services
import base_market_service


class BudaHMACAuth(requests.auth.AuthBase):
    """Adjunta la autenticación HMAC de Buda al objeto Request."""

    def __init__(self, api_key: str, secret: str):
        self.api_key = api_key
        self.secret = secret

    def get_nonce(self) -> str:
        # 1. Generar un nonce (timestamp en microsegundos)
        return str(int(time.time() * 1e6))

    def sign(self, r, nonce: str) -> str:
        # 2. Preparar string para firmar
        components = [r.method, r.path_url]
        if r.body:
            encoded_body = base64.b64encode(r.body).decode()
            components.append(encoded_body)
        components.append(nonce)
        msg = ' '.join(components)
        # 3. Obtener la firma
        h = hmac.new(key=self.secret.encode(),
                        msg=msg.encode(),
                        digestmod='sha384')
        signature = h.hexdigest()
        return signature

    def __call__(self, r):
        nonce = self.get_nonce()
        signature = self.sign(r, nonce)
        # 4. Adjuntar API-KEY, nonce y firma al header del request
        r.headers['X-SBTC-APIKEY'] = self.api_key
        r.headers['X-SBTC-NONCE'] = nonce
        r.headers['X-SBTC-SIGNATURE'] = signature
        return r


class Buda(base_market_service.BaseMarketService):

    url = 'https://www.buda.com/api/v2/'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, auth=BudaHMACAuth, **kwargs)
        self.generate_auth()

    def generate_auth(self):
        key = self.user.keys.get(self.market)
        self.auth = self.auth(key.api_key, key.api_secret)
