from decimal import Decimal

import requests
from django.conf import settings

from apps.crypto.constant import CryptoCurrency, FiatCurrency
from apps.crypto.models import ExchangeRateHistory
from apps.crypto.exceptions import UnconfiguredEnvironment


def get_newest_currency_exchange(
    from_currency: str = CryptoCurrency.BTC.name,
    to_currency: str = FiatCurrency.USD.name
) -> Decimal:
    """Return exchange rate for chosen currencies."""
    api_key = settings.ALPHAVANTAGE_EXCHANGE["API_KEY"]
    if not api_key:
        raise UnconfiguredEnvironment("Alphavantage exchange API_KEY empty or does not exist")

    exchange_url = settings.ALPHAVANTAGE_EXCHANGE["RATE_URL"].format(
        from_currency=from_currency,
        to_currency=to_currency,
        api_key=api_key
    )
    response = requests.get(exchange_url)
    data = response.json()
    exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return Decimal(exchange_rate)


def refresh_currency_exchange(
    from_currency: str = CryptoCurrency.BTC.name,
    to_currency: str = FiatCurrency.USD.name
) -> dict[str, Decimal]:
    exchange_rate = get_newest_currency_exchange(from_currency, to_currency)
    ExchangeRateHistory.objects.create(
        from_currency=from_currency,
        to_currency=to_currency,
        exchange_rate=exchange_rate
    )
    return {f"{from_currency}/{to_currency}": exchange_rate}
