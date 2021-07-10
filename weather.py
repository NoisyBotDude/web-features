import requests

def city(cities):
        api_key = "5d52a94d4dcb8a2a52599d68a443e1f7"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"

        complete_url = f"{base_url}appid={api_key}&q={cities}"
        print(complete_url)

        response = requests.get(complete_url)
        x  = response.json()

        response_main = x['main']
        response_weather = x['weather'][0]

        if response_main:
                current_tempcels = int(response_main['temp'] - 273.15)
                feels_like = int(response_main['feels_like'] - 273.15)
                response_weather_main = response_weather['main']
                print(f'Current temperature is {current_tempcels}'
                      f'It feels like {feels_like}')
                print(f'There is a chance of: {response_weather_main}')

        else:
                return f'Eroor getting temperature of {cities}'

city("Guwahati")
