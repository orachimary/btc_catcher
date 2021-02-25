from django.apps import apps
from celery import shared_task
import requests
from django.conf import settings


@shared_task
def get_btc_info():
    BTC_model = apps.get_model(app_label='gather', model_name='BTC')
    header = {
        'X-CMC_PRO_API_KEY': settings.CMC_PRO_API_KEY,
        'Accept': 'application/json'
    }
    r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1', headers=header)
    btc_json = r.json()
    usd_price = float(btc_json['data']['1']['quote']['USD']['price'])
    percent_change_1h = float(btc_json['data']['1']['quote']['USD']['percent_change_1h'])
    percent_change_24h = float(btc_json['data']['1']['quote']['USD']['percent_change_24h'])
    btc = BTC_model(usd_price = usd_price, percent_change_1h = percent_change_1h, percent_change_24h = percent_change_24h)
    btc.save()