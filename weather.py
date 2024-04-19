import requests
import json
from speak import say

# Replace with your OpenWeatherMap API key
OPENWEATHERMAP_API_KEY = "8c4a2e2abfe6e2204f3a5d31565a5178"

def get_user_ip():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("ip")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP address: {e}")
        return None

def get_user_location():
    user_ip_address = get_user_ip()
    if user_ip_address:
        url = f"https://ipinfo.io/{user_ip_address}/json"
        try:
            response = requests.get(url)
            data = response.json()
            return data.get("city", "Unknown")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching location: {e}")
            return "Unknown"
    else:
        return "Unknown"

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            weather_main = data["weather"][0]["main"]
            feels_like = data["main"]["feels_like"]
            wind_speed = data["wind"]["speed"]
            visibility = data["visibility"]
            weather_text = f"{weather_main}: The Temparature is {temperature}° Celsius right now in {city}, but it feels like {feels_like}° Celsius.\n" \
               f"The Wind is blowing at {round(wind_speed * 3.6, 2)} km/h and the Visibility is {int(visibility/ 1000)} km." 

        else:
            weather_text = "Sorry, I couldn't fetch the weather data at the moment."
    except requests.RequestException:
        weather_text = "Sorry, I couldn't fetch the weather data at the moment."
    
    say(weather_text)