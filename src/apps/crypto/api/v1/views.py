from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.crypto.api.v1.serializers import QuotesSerializer
from apps.crypto.models import ExchangeRateHistory
from apps.crypto.tasks import get_newest_exchange_rates


class QuotesAPIView(APIView):
    """APIView for get quotes of chosen currencies pairs."""

    def get(self, request, *args, **kwargs) -> Response:
        try:
            latest_quotes = ExchangeRateHistory.objects.latest("created_at")
        except ExchangeRateHistory.DoesNotExist:
            return Response(
                {"detail": ["There are no records in DB"]},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        serializer = QuotesSerializer(instance=latest_quotes)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs) -> Response:
        get_newest_exchange_rates.delay()
        return Response({"detail": ["Force requesting the prices was sent"]})


