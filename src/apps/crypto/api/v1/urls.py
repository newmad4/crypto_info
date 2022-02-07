from django.urls import include, path


from .views import QuotesAPIView


urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("quotes", QuotesAPIView.as_view(), name="quotes"),
            ]
        )
    )
]
