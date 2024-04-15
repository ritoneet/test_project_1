import requests
from currency.models import Currency


def parse_privat():
    privat_currency_url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
    responce = requests.get(privat_currency_url)
    rate = responce.json()
    privat_type_usd = rate[1].get("ccy")
    privat_buy_usd = rate[1].get("buy")
    privat_sale_usd = rate[1].get("sale")
    print(privat_type_usd, privat_sale_usd, privat_buy_usd)
    Currency.objects.create(type=privat_type_usd, sale=privat_sale_usd, buy=privat_buy_usd, source="privatbank")

    rate_list = Currency.objects.all()
    return rate_list
