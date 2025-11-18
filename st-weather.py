import streamlit as st
import requests
import pandas as pd
from datetime import datetime as date
import json

# Add your OpenWeatherMap API key here
API_KEY = 'YOUR_API_KEY_HERE'

st.title('Weather App')
city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
             'Philadelphia', 'Las Vegas', 'San Diego', 'Dallas', 
             'San Jose', 'Bozeman']
cities = st.multiselect('Select cities', city_list, default=['New York', 'Los Angeles'])
st.markdown('---')

temp_list = []
for city in cities:
    payload = {'q':city, 'APPID':API_KEY}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
    weather = r.json()

    if 'weather' in weather:
        # Convert from Kelvin to Fahrenheit
        temp_list.append((weather['main']['temp'] - 273.15) * 9/5 + 32)  
    else:
        temp_list.append(None)

st.subheader(f'Current time: {date.now()}')
df = pd.DataFrame({'City': cities, 'Temperature (°F)': temp_list})
st.table(df)

    
