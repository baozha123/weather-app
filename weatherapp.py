import requests

API_KEY = "bcc2c8f3f088ba20a181a402c5ea14e3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("weather:", weather)
    print("temperature:", temperature, "Celsius")
else :
    print("gg, error occured")
if temperature < 0:
    print('好冷')
if temperature < 10 and temperature > 0:
    print('有点冷')
if temperature < 20 and temperature >10:
    print('舒适天气')
else :
    print('好热')

