import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('data/weather.db')
cursor = conn.cursor()

# Get today's date in YYYY-MM-DD format
today = datetime.now().strftime('%Y-%m-%d')

# Query to get weather data for today
cursor.execute('''
    SELECT temperature, feels_like, condition FROM weather_data
    WHERE date_time LIKE ?
''', (today + '%',))

weather_records = cursor.fetchall()

if not weather_records:
    print("No weather data found for today.")
else:
    temperatures = [record[0] for record in weather_records]
    feels_like = [record[1] for record in weather_records]
    conditions = [record[2] for record in weather_records]

    # Calculate aggregates
    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    dominant_condition = max(set(conditions), key=conditions.count)

    print(f"Daily Weather Summary for {today}:")
    print(f"Average Temperature: {avg_temp:.2f} °C")
    print(f"Maximum Temperature: {max_temp:.2f} °C")
    print(f"Minimum Temperature: {min_temp:.2f} °C")
    print(f"Dominant Condition: {dominant_condition}")

conn.close()
