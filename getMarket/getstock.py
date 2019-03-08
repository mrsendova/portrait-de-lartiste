# coding: utf-8

import config
import requests

CleAPI = config.AlphaVantageAPIKey

reqData = {
    'function':'TIME_SERIES_DAILY_ADJUSTED',
    'symbol':'BID',
    'datatype':'csv',
    'outputsize': 'full',
    'apikey': CleAPI
}
r = requests.get('https://www.alphavantage.co/query', params=reqData)
print(r.text)
