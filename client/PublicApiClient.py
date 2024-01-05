from pybithumb import Bithumb

class PublicApiClient:
    def __init__(self):
        self.bithumb = Bithumb

    def getCurrentPrice(self, symbol):
        return self.bithumb.get_current_price(symbol)



publicApiClient=PublicApiClient()