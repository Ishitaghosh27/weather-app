#!/usr/bin/env python3
"""
Simple test script to verify OpenWeatherMap API key functionality
"""

import requests
from decouple import config

def test_api_key():
    """Test if the OpenWeatherMap API key is working"""
    
    # Get API key from .env file
    api_key = config('OPENWEATHER_API_KEY', default='')
    
    print("🔍 Testing OpenWeatherMap API Key...")
    print(f"API Key: {api_key[:10]}..." if len(api_key) > 10 else f"API Key: {api_key}")
    print("-" * 50)
    
    if not api_key:
        print("❌ No API key found in .env file")
        return False
    
    # Test with a simple city
    test_city = "London"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': test_city,
        'appid': api_key,
        'units': 'metric',
    }
    
    try:
        print(f"🌍 Testing with city: {test_city}")
        response = requests.get(base_url, params=params, timeout=10)
        
        print(f"📡 Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API Key is working!")
            print(f"📍 City: {data['name']}, {data['sys']['country']}")
            print(f"🌡️ Temperature: {data['main']['temp']}°C")
            print(f"☁️ Weather: {data['weather'][0]['description']}")
            print(f"💧 Humidity: {data['main']['humidity']}%")
            return True
            
        elif response.status_code == 401:
            print("❌ API Key is invalid or unauthorized")
            print("💡 Make sure your API key is correct and activated")
            return False
            
        elif response.status_code == 429:
            print("⚠️ Rate limit exceeded")
            print("💡 Wait a few minutes and try again")
            return False
            
        else:
            print(f"❌ Unexpected error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_multiple_cities():
    """Test API with multiple cities"""
    
    api_key = config('OPENWEATHER_API_KEY', default='')
    if not api_key:
        print("❌ No API key found")
        return
    
    cities = ["London", "New York", "Tokyo", "Paris", "Raipur"]
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    print("\n🌍 Testing multiple cities...")
    print("-" * 50)
    
    for city in cities:
        try:
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric',
            }
            
            response = requests.get(base_url, params=params, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ {city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
            else:
                print(f"❌ {city}: Error {response.status_code}")
                
        except Exception as e:
            print(f"❌ {city}: {e}")

if __name__ == "__main__":
    print("🚀 OpenWeatherMap API Key Test")
    print("=" * 50)
    
    # Test basic functionality
    if test_api_key():
        print("\n" + "=" * 50)
        # Test multiple cities
        test_multiple_cities()
    
    print("\n" + "=" * 50)
    print("�� Test completed!")
