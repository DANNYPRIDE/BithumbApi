from client.PrivateApiClient import privateApiClient
from client.PublicApiClient import publicApiClient

btcUnitPrice = 1000

while True:

    try:
        (remainingBtc, lockedBtc, remainingKrw, lockedKrw) = privateApiClient.getBalance("BTC")
        currentPrice = publicApiClient.getCurrentPrice("BTC")
    except Exception as e:
        continue
    buyOrder = privateApiClient.buyOrder(price=int(currentPrice - btcUnitPrice * 4),
                                         unit=(remainingKrw / 4) / currentPrice)
    sellOrder = privateApiClient.sellOrder(price=int(currentPrice + btcUnitPrice * 4), unit=remainingBtc / 4)

    buyOrder2 = privateApiClient.buyOrder(price=int(currentPrice - btcUnitPrice * 8),
                                      unit=(remainingKrw / 4) / currentPrice)
    sellOrder2 = privateApiClient.sellOrder(price=int(currentPrice + btcUnitPrice * 8), unit=remainingBtc / 4)

    buyOrder3 = privateApiClient.buyOrder(price=int(currentPrice - btcUnitPrice * 12),
                                      unit=(remainingKrw / 4) / currentPrice)
    sellOrder3 = privateApiClient.sellOrder(price=int(currentPrice + btcUnitPrice * 12), unit=remainingBtc / 4)

    buyOrder4 = privateApiClient.buyOrder(price=int(currentPrice - btcUnitPrice * 16),
                                      unit=(remainingKrw / 4) / currentPrice)
    sellOrder4 = privateApiClient.sellOrder(price=int(currentPrice + btcUnitPrice * 16), unit=remainingBtc / 4)

    privateApiClient.cancelOrder(buyOrder)
    privateApiClient.cancelOrder(sellOrder)
    privateApiClient.cancelOrder(buyOrder2)
    privateApiClient.cancelOrder(sellOrder2)
    privateApiClient.cancelOrder(buyOrder3)
    privateApiClient.cancelOrder(sellOrder3)
    privateApiClient.cancelOrder(buyOrder4)
    privateApiClient.cancelOrder(sellOrder4)