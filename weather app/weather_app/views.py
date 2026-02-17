from django.shortcuts import render
from django.http import JsonResponse
import requests
from decouple import config
import json
import random
from django.conf import settings

def city_suggestions(request):
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse([], safe=False)
    
    api_key = settings.OPENWEATHER_API_KEY
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Extract "City, Country" format
        cities = [f"{item['name']}, {item['country']}" for item in data]
        return JsonResponse(cities, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def index(request):
    """
    Main view for the weather app homepage.
    Handles both GET (display form) and POST (fetch weather data) requests.
    """
    weather_data = None
    error_message = None
    
    if request.method == 'POST':
        # Get city name from form submission
        city = request.POST.get('city', '').strip()
        
        if city:
            # Try to fetch real weather data, fall back to mock data if API key is not set
            weather_data, error_message = get_weather_data(city)
    
    # Context data to pass to template
    context = {
        'weather_data': weather_data,
        'error_message': error_message,
    }
    
    return render(request, 'weather_app/index.html', context)

def get_weather_data(city):
    """
    Fetch weather data from OpenWeatherMap API for a given city.
    Falls back to mock data if API key is not properly configured.
    
    Args:
        city (str): Name of the city to get weather for
        
    Returns:
        tuple: (weather_data_dict, error_message) - weather data if successful, error message if failed
    """
    # Get API key from environment variables
    api_key = config('OPENWEATHER_API_KEY', default='')
    
    # Check if API key is properly set (not the placeholder)
    if not api_key or api_key == 'your_api_key_here' or api_key == 'YOUR_ACTUAL_API_KEY_HERE' or len(api_key) < 20:
        # Return mock data for demonstration
        print(f"🔍 Using mock data - API key: {api_key[:10]}...")
        return get_mock_weather_data(city), None
    
    print(f"🔍 Using real API - API key: {api_key[:10]}...")
    
    # OpenWeatherMap API endpoint for current weather
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Use Celsius for temperature
    }
    
    try:
        # Make API request
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse JSON response
        data = response.json()
        
        # Extract relevant weather information
        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),  # Round to nearest integer
            'description': data['weather'][0]['description'].title(),
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'feels_like': round(data['main']['feels_like']),
        }
        
        return weather_data, None
        
    except requests.exceptions.RequestException as e:
        # Handle network/API errors
        error_message = f"Error fetching weather data: {str(e)}"
        return None, error_message
        
    except KeyError as e:
        # Handle missing data in API response
        error_message = f"Unexpected API response format: {str(e)}"
        return None, error_message
        
    except json.JSONDecodeError:
        # Handle invalid JSON response
        error_message = "Invalid response from weather service"
        return None, error_message

def get_mock_weather_data(city):
    """
    Generate mock weather data for demonstration purposes.
    This function provides realistic sample data when no API key is available.
    
    Args:
        city (str): Name of the city
        
    Returns:
        dict: Mock weather data
    """
    # Sample weather conditions
    weather_conditions = [
        {'description': 'Clear Sky', 'icon': '01d', 'temp_range': (15, 30)},
        {'description': 'Partly Cloudy', 'icon': '02d', 'temp_range': (12, 25)},
        {'description': 'Cloudy', 'icon': '03d', 'temp_range': (10, 22)},
        {'description': 'Light Rain', 'icon': '10d', 'temp_range': (8, 18)},
        {'description': 'Thunderstorm', 'icon': '11d', 'temp_range': (5, 15)},
        {'description': 'Snow', 'icon': '13d', 'temp_range': (-5, 5)},
        {'description': 'Mist', 'icon': '50d', 'temp_range': (10, 20)},
    ]
    
    # Select a random weather condition
    condition = random.choice(weather_conditions)
    
    # Generate temperature within the range
    temp_min, temp_max = condition['temp_range']
    temperature = random.randint(temp_min, temp_max)
    feels_like = temperature + random.randint(-3, 3)
    
    # Generate other weather data
    humidity = random.randint(40, 90)
    wind_speed = round(random.uniform(0, 15), 1)
    
    # Mock country codes
    countries = ['US', 'GB', 'IN', 'CA', 'AU', 'DE', 'FR', 'JP', 'BR', 'CN']
    country = random.choice(countries)
    
    return {
        'city': city.title(),
        'country': country,
        'temperature': temperature,
        'description': condition['description'],
        'icon': condition['icon'],
        'humidity': humidity,
        'wind_speed': wind_speed,
        'feels_like': feels_like,
        'is_mock': True,  # Flag to indicate this is mock data
    }
