class Buda:
    
    def __init__(self, user):
        self.user = user
        self.api_key = user.api_key
        self.api_secret = user.api_secret