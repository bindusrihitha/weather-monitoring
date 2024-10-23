import sqlite3
from datetime import datetime

# Define alert thresholds
TEMPERATURE_THRESHOLD = 35  # Example threshold in Celsius

# Connect to the SQLite database
conn = sqlite3.connect('data/weather.db')
cursor = conn.cursor()

# Get the latest weather data
cursor.execute('''
    SELECT temperature, date_time FROM weather_data
    ORDER BY date_time DESC LIMIT 1
''')
latest_record = cursor.fetchone()

if latest_record:
    latest_temp = latest_record[0]
    latest_time = latest_record[1]
    print(f"Latest Temperature: {latest_temp} °C at {latest_time}")

    # Check if the temperature exceeds the threshold
    if latest_temp > TEMPERATURE_THRESHOLD:
        print("Alert! Temperature exceeds the defined threshold.")

else:
    print("No weather data found.")

conn.close()
