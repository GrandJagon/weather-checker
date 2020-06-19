#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:19:01 2020

@author: lucas
"""

def kalvin_to_celsius(kalv):
    return kalv - 273.15

from gethostinfo import get_local_info, get_external_info
import requests as rq

key = "e7ae282006ca7833cc59a54fe8a26595"

url = "https://api.openweathermap.org/data/2.5/weather"

result = "The current weather at {} in {} is {} with a temperature of {} degrees celsius"



while True:
    user_input = input("Type 1 to use the weather checker for you current location, 2 to enter a geographical location or 3 to enter an IP")
    if user_input == '1':
        user_info = get_local_info()
        city = user_info["city"]
        break
    elif user_input == '2':
        city = input("Please enter a location")
        break
    elif user_input == '3':
        manual_ip = input("Please enter a valid IP address")
        user_info = get_external_info(manual_ip)
        city = user_info['city']
        break
    else:
        print("Please enter a valid answer")
        
        
parameters = {'q' : city, "appid" : key}

json = rq.get(url, params = parameters).json()

temp = kalvin_to_celsius(json['main']['temp'])

print(result.format(json['name'], json['sys']['country'], json['weather'][0]['description'], temp))



