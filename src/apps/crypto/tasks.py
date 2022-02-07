from decimal import Decimal

from crypto_info.celery import app
from apps.crypto.utils import refresh_currency_exchange


@app.task(name="get_newest_exchange_rates")
def get_newest_exchange_rates() -> dict[str, Decimal]:
    """Periodic task for fetch newest exchange rate of some currencies."""
    return refresh_currency_exchange()
