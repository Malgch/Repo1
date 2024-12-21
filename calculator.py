from pprint import pprint
import requests
import os

def get_exchange_rate(currency_code ="EUR"):
    try:
        url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/?format=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates'][0]['mid']  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None