from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('data/weather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather_data ORDER BY date_time DESC LIMIT 1")
    weather = cursor.fetchone()
    conn.close()
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
