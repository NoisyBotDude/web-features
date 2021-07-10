import requests

api_key = "199e11199b8fef9f74b6"
base_url = "https://free.currconv.com/api/v7/"

print("You need the currency code to convert any currrency to teh other\n"
      "If yoy don't know such id, you can download it\n")
confirmation = str(input("Enter YES to download the codes in txt format: "))

if confirmation.lower() == "yes":
    print("Hello")

from_currency = str(input("Enter the currency Id which you want to convert: "))
to_currency = str(input("Enter the currrency Id you wan to conver to: "))
from_to_currency = f'{from_currency}_{to_currency}'
to_from_currency = f'{to_currency}_{from_currency}'

complete_url = f'{base_url}convert?apiKey={api_key}&q={from_to_currency},{to_from_currency}'

response = requests.get(complete_url)
x  = response.json()

response_from_to = x['results'][f'{from_to_currency}']
response_to_from = x['results'][f'{to_from_currency}']
#response_weather = x['weather'][0]

if response_from_to:
    response_to_value = response_from_to['val']
    response_from_value = response_to_from['val']

    print(f'{from_currency} to {to_currency}: {response_to_value}')
    print(f'{to_currency} to {from_currency}:  {response_from_value}')

else:
          print("Hello")


