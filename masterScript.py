import requests
from datetime import datetime
import excelScript
import emailsender

user_api = "d070f8e62beaa276f2f4134945c1b01a"


def city_forecast(location):
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    # create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    excelScript.excelClass(location)
    for i in range(0, len(excelScript.maillist)):
        if humidity != 100:
            emailsender.sendMail(excelScript.maillist[i])


cities = excelScript.citylist
cities = list(set(cities))

for k in range(0, len(cities)):
    city_forecast(cities[k])
