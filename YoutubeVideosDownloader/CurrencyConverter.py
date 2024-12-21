##Currency Converter,Convert USD to INR using live exchange rates
##Currency Converter,Convert GBP to INR using live exchange rates
##Currency Converter,Convert AED to INR using live exchange rates

import requests
from_curr = 'GBP'
to_curr = 'INR'
url = 'https://api.exchangerate-api.com/v4/latest/' + from_curr
response = requests.get(url)
rates = response.json()
print(f"1 {from_curr} = {rates['rates'][to_curr]} {to_curr}")


