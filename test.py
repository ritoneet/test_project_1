def parse_privat():
    import requests
    privat_currency_url="https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
    responce = requests.get(privat_currency_url)
    rate = responce.json()
    print(rate)

parse_privat()
# import decimal
# a = decimal.Decimal('1.1')
# b = decimal.Decimal('1.1')
# c = decimal.Decimal('1.1')
#
# print(type(a))
# print((a+b+c))