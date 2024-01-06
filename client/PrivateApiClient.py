from pybithumb import Bithumb


class PrivateApiClient:
    def __init__(self):
        self.bithumb = Bithumb("", "")

    def findFee(self, symbol):
        print(self.bithumb.get_trading_fee(symbol))

    #(보유코인, 사용중코인, 보유원화, 사용중원화)
    def getBalance(self, symbol):
        return self.bithumb.get_balance(symbol)

    def buyOrder(self, price, unit):
        return self.bithumb.buy_limit_order("BTC", price, unit)

    def sellOrder(self, price, unit):
        return self.bithumb.sell_limit_order("BTC", price, unit)

    def getReaminingOrder(self, order):
        return self.bithumb.get_outstanding_order(order)

    def cancelOrder(self, order):
        return self.bithumb.cancel_order(order)

privateApiClient = PrivateApiClient()