import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('data/weather.db')
cursor = conn.cursor()

# Fetch weather data
cursor.execute('''
    SELECT date_time, temperature FROM weather_data
''')
data = cursor.fetchall()

if not data:
    print("No weather data found.")
    conn.close()
    exit()

# Prepare data for plotting
dates = [datetime.strptime(record[0], '%Y-%m-%d %H:%M:%S') for record in data]
temperatures = [record[1] for record in data]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(dates, temperatures, marker='o', linestyle='-', color='b')
plt.title('Weather Temperature Over Time')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

# Show the plot
plt.show()

conn.close()
