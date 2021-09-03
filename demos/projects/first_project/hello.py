import requests
import json
import sqlalchemy

resp = requests.get('https://weather.talkpython.fm/api/weather?city=trafalgar&state=OR&country=AU&units=Metric')
resp.raise_for_status()

data = resp.json()
temp = data['forecast']['temp']
location = data['location']['city']

print(f"Hello world it's {temp} Celsius outside in {location}!")
