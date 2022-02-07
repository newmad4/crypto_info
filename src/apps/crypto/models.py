from django.db import models


class ExchangeRateHistory(models.Model):
    """Model for store exchange rate of chosen pair."""

    created_at = models.DateTimeField(auto_now_add=True)
    exchange_rate = models.DecimalField(max_digits=18, decimal_places=8)
    from_currency = models.CharField(max_length=10)
    to_currency = models.CharField(max_length=10)
