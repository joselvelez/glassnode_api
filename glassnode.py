import json
import requests
import pandas as pd

API_KEY = ''

result = requests.get('https://api.glassnode.com/v1/metrics/indicators/sopr',
    params={'a': 'BTC', 'api_key': API_KEY})

print(result.text)