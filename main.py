from client.PrivateApiClient import privateApiClient
from client.PublicApiClient import publicApiClient

btcUnitPrice = 1000
orderList = []

while True:

    (remainingBtc, lockedBtc, remainingKrw, lockedKrw) = privateApiClient.getBalance("BTC")
    currentPrice = publicApiClient.getCurrentPrice("BTC")

    for i in range(1, 5):
        buyOrder = privateApiClient.buyOrder(price=int(currentPrice - btcUnitPrice * i * 1),
                                             unit=(remainingKrw/4) / currentPrice)
        sellOrder = privateApiClient.sellOrder(price=int(currentPrice + btcUnitPrice * i * 1), unit=remainingBtc / 4)
        orderList.append(buyOrder)
        orderList.append(sellOrder)

    while len(orderList) > 0:
        privateApiClient.cancelOrder(orderList.pop())