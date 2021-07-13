import requests

api_key = "5d52a94d4dcb8a2a52599d68a443e1f7"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
cities = ['Guwahati', 'Dehli', 'Tezpur']
current_temperature = []
status = []
wind = []
humidity = []
feels_like = []

for city in range(len(cities)):
        complete_url = f"{base_url}appid={api_key}&q={cities[city]}"
        response = requests.get(complete_url)
        json_response = response.json()

        main = json_response['main']
        weather_status = json_response['weather'][0]['main']
        wind_speed = int(json_response['wind']['speed'] * 1.85)

        current_tempcels = int(main['temp'] - 273.15)
        humidity_status = main['humidity']
        feels_like_status = int(main['feels_like'] - 273.15)

        current_temperature.append(current_tempcels)
        status.append(weather_status)
        wind.append(wind_speed)
        humidity.append(humidity_status)
        feels_like.append(feels_like_status)

