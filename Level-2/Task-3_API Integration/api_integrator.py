import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        current = data["current_condition"][0]

        print("\nWeather Information")
        print(f"City: {city}")
        print(f"Temperature: {current['temp_C']} °C")
        print(f"Weather: {current['weatherDesc'][0]['value']}")
        print(f"Humidity: {current['humidity']}%")

    except requests.exceptions.RequestException:
        print("Error: Unable to fetch weather data")


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
