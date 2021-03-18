#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import datetime

# API call
latitude = " "  # enter latitude. this can be found here: https://www.latlong.net/
longitude = " "  # enter longitude. this can be found here: https://www.latlong.net/
api_url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + latitude + "&lon=" + longitude + \
          "&units=metric&appid=18f7a9c1a5b147c35426859210480afc"


# API response as JSON
data = requests.get(api_url).json()

# grab relevant data from the json api response
temp = data['current']['temp']
feels_like = data['current']['feels_like']
sunrise = data['current']['sunrise']  # sunrise time
description = data['current']['weather'][0]['description']  # description of weather

# print relevant data from the json api response
print(datetime.date.today().strftime('| %B %d, 20%y'))
print("| The weather is", description)
print("| Sunrise time is " + datetime.datetime.fromtimestamp(int(sunrise)).strftime('%l:%Mam'))  # sunrise time x:xx am
print("| Temperature is", str(round(temp, 1)) + "c")  # temperature rounded to 1 decimal place. Shown in C
print("| Feels like", str(round(feels_like, 1)) + "c")  # temperature rounded to 1 decimal place. Shown in C




