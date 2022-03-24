import requests
import json

base = 'https://fapi.binance.com'
path = '/fapi/v1/ticker/bookTicker'
url = base + path


# request to api
class GetPrice:

    @staticmethod
    def get_price(name):
        param = {'symbol': name}
        r = requests.get(url, params=param)
        if r.status_code == 200:
            # data = json.dumps(r.json(), sort_keys=True, indent=1) // prettier json formatter
            return r.json()
        else:
            return 'error'
