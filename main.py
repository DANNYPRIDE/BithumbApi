from client.PrivateApiClient import privateApiClient
from client.PublicApiClient import publicApiClient

btcUnitPrice = 1000
orderList = []

while True:

    (remainingBtc, lockedBtc, remainingKrw, lockedKrw) = privateApiClient.getBalance("BTC")
    currentPrice = publicApiClient.getCurrentPrice("BTC")

    for i in range(1, 6):
        buyOrder = privateApiClient.buyOrder(price=int(currentPrice - btcUnitPrice * i * 4),
                                             unit=(remainingKrw/5) / currentPrice)
        sellOrder = privateApiClient.sellOrder(price=int(currentPrice + btcUnitPrice * i * 4), unit=remainingBtc / 5)
        if type(buyOrder) is tuple:
            orderList.append(buyOrder)
        if type(sellOrder) is tuple:
            orderList.append(sellOrder)

    for orders in orderList:
        privateApiClient.cancelOrder(orders)