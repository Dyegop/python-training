import json
import sys
import time
from clients.openweather import OpenWeatherClient
from clients.openexchange import OpenExchangeClient




if __name__ == '__main__':
    api_keys = [v[1] for v in json.load(open("data/api-keys.json", "r")).items()]
    url_openweather = 'http://api.openweathermap.org/data/2.5/'
    url_openexchange = 'https://openexchangerates.org/api/'

    if len(sys.argv) == 3:
        location = ''.join(sys.argv[1:])
        suffix_openweather = f'weather?q={location}&APPID={api_keys[0]}'
        print(location)
        while True:
            openweather = OpenWeatherClient(url_openweather, suffix_openweather)
            openweather.forecast(location)
            time.sleep(10)

    if len(sys.argv) == 4:
        suffix_openexchange = f'latest.json?app_id={api_keys[1]}'
        _ignore, from_amount, from_currency, to_currency = sys.argv
        openexchange = OpenExchangeClient(url_openexchange, suffix_openexchange)
        print(openexchange.convert(float(from_amount), from_currency, to_currency))

    else:
        print('Usage for Open Weather API: filename.py City_name, 2-letter_Country_code')
        print('Example: openAPIs.py Madrid, ES\n')
        print('Usage for Open Exchange API: filename.py from_amount, from_currency, to_currency')
        print('Example: openAPIs.py 1000, EUR, USD\n')
        sys.exit()
