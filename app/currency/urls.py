from django.urls import path
from currency.views import CurrencyRateCreate


urlpatterns = [
    path("currency", CurrencyRateCreate.as_view(), name="rate-link"),
    ]
