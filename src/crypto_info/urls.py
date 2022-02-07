"""crypto_info URL Configuration"""
from django.urls import path, include

urlpatterns = [
    path("api/", include(
            [
                path("", include("apps.crypto.api.v1.urls")),
            ]
        )
    )
]
