from rest_framework import serializers


class QuotesSerializer(serializers.Serializer):
    exchange_rate = serializers.DecimalField(read_only=True, decimal_places=8, max_digits=18)
    from_currency = serializers.CharField(read_only=True)
    to_currency = serializers.CharField(read_only=True)
