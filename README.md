# Weather Monitoring System

## Description
The Weather Monitoring System is a Flask application that retrieves real-time weather data from the Visual Crossing API and stores it in an SQLite database. It features email alerts for critical temperature thresholds and provides a web interface for visualizing weather data using Matplotlib.

## Features
- Fetches current weather data from Visual Crossing API.
- Stores weather information in an SQLite database.
- Sends email alerts when temperature exceeds specified thresholds.
- User-friendly web interface for displaying the latest weather updates and visualizations.

## Installation
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd weather-monitoring`
3. Set up a virtual environment: `python -m venv venv`
4. Activate the virtual environment: 
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Usage
Run the application with: `python app.py` and navigate to `http://127.0.0.1:5000` in your browser.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
