from django.shortcuts import render
from django.views.generic import TemplateView
from currency.utils import parse_privat


class CurrencyRateCreate(TemplateView):
    template_name = "currency.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = parse_privat()
        return context

