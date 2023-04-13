import sys
import os

from io import BytesIO
from datetime import datetime

import configparser as cp
import pycurl

import wttr_conditions


# Env vars
this_folder = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(this_folder, 'env')
vars = cp.ConfigParser()
vars.read(config_file)
LOCATION = vars.get("vars", "LOCATION")
WEATHER_ICONS = vars.get("vars", "WEATHER_ICONS")


def get_weather(location: str, endpoint: str) -> str:
    c = pycurl.Curl()
    buffer = BytesIO()
    c.setopt(c.URL, f'https://en.wttr.in/{location}?format={endpoint}')
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    value = buffer.getvalue().decode('UTF-8')
    return value


def parse_temp(temperature: str) -> str:
    if temperature[0] == '+':  # remove the leading plus from temps above zero
        temperature = temperature[1:]
    elif temperature == '-0°C':  # no such thing as minus zero
        temperature = '0°C'
    return temperature


def parse_wind(wind_speed: str) -> str:
    match wind_speed[0]:
        case '↑':
            wind_speed = f'N at {wind_speed[1:]}'
        case '↗':
            wind_speed = f'NE at {wind_speed[1:]}'
        case '→':
            wind_speed = f'E at {wind_speed[1:]}'
        case '↘':
            wind_speed = f'SE at {wind_speed[1:]}'
        case '↓':
            wind_speed = f'S at {wind_speed[1:]}'
        case '↙':
            wind_speed = f'SW at {wind_speed[1:]}'
        case '←':
            wind_speed = f'W at {wind_speed[1:]}'
        case '↖':
            wind_speed = f'NW at {wind_speed[1:]}'
        case _:
            print(f'It shouldn\'t happen - en.wttr.in has passed unsupported case - {wind_speed[0]}')
            sys.exit(1)
    return wind_speed


def parse_location(location: str) -> str:
    location = location.replace('+', ' ')
    location = location.capitalize()
    return location


def parse_conditions(condition: str) -> str:
    condition_check = condition.casefold()
    if condition_check in wttr_conditions.clear:
        condition = ''
    elif condition_check in wttr_conditions.clouds:
        condition = ''
    elif condition_check in wttr_conditions.fog:
        condition = ''
    elif condition_check in wttr_conditions.heavy_rain:
        condition = ''
    elif condition_check in wttr_conditions.rain:
        condition = ''
    elif condition_check in wttr_conditions.rain_and_snow:
        condition = ''
    elif condition_check in wttr_conditions.snow:
        condition = ''
    elif condition_check in wttr_conditions.thunder:
        condition = ''
    elif condition_check in wttr_conditions.thunder_snow:
        condition = ''
    elif condition_check in wttr_conditions.thunder_rain:
        condition = ''
    else:
        condition = f'It shouldn\'t happen - en.wttr.in has passed unsupported case - {condition}'
    return condition


# Define print functions for Conky
def print_location():
    print(parse_location(LOCATION))


def print_conditions():
    if WEATHER_ICONS == 'true':
        print(parse_conditions(get_weather(LOCATION, '%C')))
    else:
        print(get_weather(LOCATION, '%C'))


def print_precipitation():
    print(get_weather(LOCATION, '%p'))


def print_pressure():
    print(get_weather(LOCATION, '%P'))


def print_humidity():
    print(get_weather(LOCATION, '%h'))


def print_wind():
    print(parse_wind(get_weather(LOCATION, '%w')))


def print_temp():
    print(parse_temp(get_weather(LOCATION, '%t')))


def print_feel():
    print(parse_temp(get_weather(LOCATION, '%f')))


def print_sunrise():
    print(get_weather(LOCATION, '%S'))


def print_sunset():
    print(get_weather(LOCATION, '%s'))


def print_update_time():
    print(datetime.now().strftime('%H:%M:%S'))


if __name__ == '__main__':
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2] = function args : (*unpacked)
    globals()[args[1]](*args[2:])
