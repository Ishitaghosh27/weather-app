# Weather App

A beautiful and responsive Django weather application that provides real-time weather information for any city using the OpenWeatherMap API.

## Features

- 🌍 **City Search**: Search for weather information by city name
- 🌡️ **Real-time Data**: Get current temperature, weather description, and conditions
- 🎨 **Beautiful UI**: Modern, responsive design with Bootstrap and custom CSS
- 📱 **Mobile Friendly**: Optimized for all device sizes
- 🎯 **Error Handling**: Graceful error messages for invalid cities or API issues
- 🔒 **Secure**: API key stored in environment variables

## Screenshots

The app features a clean, modern interface with:
- Gradient background
- Card-based layout
- Weather icons from OpenWeatherMap
- Responsive design for mobile and desktop

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone or download the project**
   ```bash
   # If you have the project files, navigate to the project directory
   cd "weather app"
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   
   a. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   
   b. Edit the `.env` file in the project root:
   ```
   # OpenWeatherMap API Key
   # Get your free API key from: https://openweathermap.org/api
   OPENWEATHER_API_KEY=your_actual_api_key_here
   ```
   
   Replace `your_actual_api_key_here` with your real API key.

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   
   Navigate to `http://127.0.0.1:8000/` to see the weather app in action!

## Usage

1. **Search for a city**: Enter any city name in the search box
2. **View weather data**: The app will display:
   - City name and country
   - Current temperature in Celsius
   - Weather description (e.g., "Clear Sky", "Cloudy")
   - Weather icon
   - Humidity percentage
   - Wind speed in m/s
   - "Feels like" temperature

3. **Error handling**: If a city is not found, the app will display a helpful error message

## Project Structure

```
weather app/
├── weather_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py
├── weather_app/             # Weather app
│   ├── __init__.py
│   ├── views.py             # View logic and API calls
│   ├── urls.py              # App URL routing
│   └── apps.py
├── templates/               # HTML templates
│   └── weather_app/
│       └── index.html       # Main template
├── static/                  # Static files
│   └── css/
│       └── style.css        # Custom CSS styling
├── .env                     # Environment variables (API key)
├── requirements.txt         # Python dependencies
├── manage.py               # Django management script
└── README.md               # This file
```

## API Configuration

The app uses the OpenWeatherMap API with the following configuration:
- **Endpoint**: `http://api.openweathermap.org/data/2.5/weather`
- **Units**: Metric (Celsius)
- **Rate Limit**: 60 calls/minute for free tier

## Customization

### Styling
- Edit `static/css/style.css` to customize colors, fonts, and layout
- The app uses Bootstrap 5.3.0 for responsive design
- Font Awesome icons are included for enhanced UI

### Features
- Modify `weather_app/views.py` to add more weather data fields
- Update the template in `templates/weather_app/index.html` to change the layout
- Add new API endpoints in `weather_app/urls.py`

## Troubleshooting

### Common Issues

1. **"API key not found" error**
   - Make sure your `.env` file exists and contains the correct API key
   - Verify the API key is valid on OpenWeatherMap

2. **"City not found" error**
   - Check the spelling of the city name
   - Try using the full city name (e.g., "New York" instead of "NYC")

3. **Static files not loading**
   - Run `python manage.py collectstatic` if needed
   - Check that the static files directory is properly configured

4. **Server won't start**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check that you're in the correct directory with `manage.py`

## Dependencies

- **Django 4.2.7**: Web framework
- **python-decouple 3.8**: Environment variable management
- **requests 2.31.0**: HTTP library for API calls

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- [Bootstrap](https://getbootstrap.com/) for the responsive CSS framework
- [Font Awesome](https://fontawesome.com/) for the icons
