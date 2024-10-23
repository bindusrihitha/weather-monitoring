import sqlite3

# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('data/weather.db')
cursor = conn.cursor()

# Create table to store weather data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        date_time TEXT,
        temperature REAL,
        feels_like REAL,
        condition TEXT
    )
''')

conn.commit()
print("Database setup complete.")
conn.close()
