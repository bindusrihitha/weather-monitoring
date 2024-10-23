import requests
import sqlite3
from datetime import datetime

API_KEY = "H4BVG9PQQNVNVBET996SSVAA4"  # Replace with your actual key
CITY = "Bangalore"  # Change as needed
URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{CITY}?unitGroup=metric&key={API_KEY}"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    current = data['currentConditions']

    # Extract relevant fields
    temperature = current['temp']
    feels_like = current['feelslike']
    condition = current['conditions']
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Store the data in SQLite database
    conn = sqlite3.connect('data/weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather_data (city, date_time, temperature, feels_like, condition)
        VALUES (?, ?, ?, ?, ?)
    ''', (CITY, date_time, temperature, feels_like, condition))
    conn.commit()
    print(f"Weather data for {CITY} stored successfully.")
    conn.close()
else:
    print("Failed to fetch weather data.")
