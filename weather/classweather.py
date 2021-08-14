import requests

class Weather:
    def __init__(self, api_key, base_url, city):
        self.api_key = api_key
        self.base_url = base_url
        self.city = city
        # self.cities = []

    # def addCity(self, city):
       # return self.cities.append(city)

    def addCity(self, city):
        self.city = city
        return self.city

    def completeUrl(self):
        return f"{self.base_url}appid={self.api_key}&q={self.city}"

    def response(self):
        return requests.get(self.completeUrl()).json()

    def currentTemperature(self):
        return int(self.response()['main']['temp'] - 273.15)

    def status(self):
        return self.response()['weather'][0]['main']

    def wind(self):
        return int(self.response()['wind']['speed'] * 1.85)

    def humidity(self):
        return self.response()['main']['humidity']

    def feelsLike(self):
        return int(self.response()['main']['feels_like'] - 273.15)

# weather = Weather("5d52a94d4dcb8a2a52599d68a443e1f7",
                  # "https://api.openweathermap.org/data/2.5/weather?", "Udalguri")
# w1 = weather.addCity("Guwahati")
# print(weather.currentTemperature())

