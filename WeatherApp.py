import requests

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    complete_url = base_url + city + '&appid=' + api_key + '&units=metric'
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data['cod'] == 200:
        weather_info = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return weather_info
    else:
        return None

def display_weather(weather):
    if weather:
        print(f"Weather: {weather['description']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or error fetching data.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_info = get_weather(city_name)
    display_weather(weather_info)
