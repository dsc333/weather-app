import requests
import json

API_KEY = 'YOUR_API_KEY_HERE'
city = input('Input city: ')

payload = {'q':city, 'APPID':API_KEY}
r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
weather = r.json()

if 'weather' in weather:
    print(f'The weather condition in {city} is {weather['weather'][0]['description']}.')
else:
    print('No weather information retrieved. Check if city and API Key are valid.') 

print('\n\nFull weather data:')
print(json.dumps(weather, indent=4))
