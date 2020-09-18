import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
from datetime import datetime
Bitcoin_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
IFTT_WEB_URL = 'https://maker.ifttt.com/trigger/Bitcoin_price_updates/with/key/bQlaGYnfNWbBamTlh9sxLP'
def bitcoin_price():
  parameters = {
    'start':'1',
    
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
  }

  session = Session()
  session.headers.update(headers)


  response = session.get(Bitcoin_API_URL, params=parameters)
  data = json.loads(response.text)
  return data['bpi']['USD']['rate_float']

def send_message_on_telegram(price):
  price_to_send = {'value1':price}

  ifttt_webhook_url = 'https://maker.ifttt.com/trigger/Bitcoin_price_update/with/key/bQlaGYnfNWbBamTlh9sxLP'
  response = requests.post(ifttt_webhook_url,json=price_to_send)
  print(response)

def run_app():
  while True:
    price = float(bitcoin_price())
    if(price<10000):
      msg = 'EMERGENCY'
      send_message_on_telegram(msg)
    else:
      send_message_on_telegram(price)
    time.sleep(30)

run_app()
