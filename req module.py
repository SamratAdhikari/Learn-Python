# Request Module

import requests

r = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=demo")
print(r.text)
# print(r.status_code) --> 200 --> successful

url = "www.something.com"
data = {
    "p1" : 4,
    "p2" : "samrat"
}
r2 = requests.post(url = url , data = data)
