# weather_visualization.py

import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import json

# ========== Step 1: Setup ==========
API_KEY = 'your_api_key_here'  # <- Replace this with your actual key
CITY = 'Hyderabad'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# ========== Step 2: Fetch Data ==========
response = requests.get(URL)
data = response.json()

# ========== Step 3: Parse Data ==========
dates = []
temps = []
weather = []

for item in data['list']:
    dt = datetime.datetime.fromtimestamp(item['dt'])
    temp = item['main']['temp']
    main_weather = item['weather'][0]['main']

    dates.append(dt)
    temps.append(temp)
    weather.append(main_weather)

# ========== Step 4: Temperature Forecast Plot ==========
plt.figure(figsize=(14, 6))
sns.lineplot(x=dates, y=temps, marker='o')
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig('temperature_forecast.png')
plt.show()

# ========== Step 5: Weather Frequency Bar Plot ==========
plt.figure(figsize=(8, 5))
sns.countplot(x=weather, palette='pastel')
plt.title(f'Weather Condition Frequency in Next 5 Days - {CITY}')
plt.xlabel('Weather Condition')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('weather_condition_frequency.png')
plt.show()

# ========== Step 6: Save Data ==========
with open('weather_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print(\"✅ Done! Check the plots and JSON file.\")
