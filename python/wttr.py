import sys
import os

from io import BytesIO
from datetime import datetime

import pycurl

import configparser as cp


def get_weather(location: str, endpoint: str) -> str:
    c = pycurl.Curl()
    buffer = BytesIO()
    c.setopt(c.URL, f'https://en.wttr.in/{location}?format={endpoint}')
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    value = buffer.getvalue().decode('UTF-8')
    return value


# Get config
this_folder = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(this_folder, 'env')
vars = cp.ConfigParser()
vars.read(config_file)

# Set vars
LOCATION = vars.get("vars", "LOCATION")

# Get all data
conditions = get_weather(LOCATION, '%C')
precipitation = get_weather(LOCATION, '%p')
pressure = get_weather(LOCATION, '%P')
humidity = get_weather(LOCATION, '%h')
wind = get_weather(LOCATION, '%w')
temp = get_weather(LOCATION, '%t')
feel = get_weather(LOCATION, '%f')
sunrise = get_weather(LOCATION, '%S')
sunset = get_weather(LOCATION, '%s')
update_time = datetime.now().strftime('%H:%M:%S')


# Parse the data to my liking
def parse_temp(temperature: str) -> str:
    if temperature[0] == '+':  # remove the leading plus from temps above zero
        temperature = temperature[1:]
    elif temperature == '-0°C':  # no such thing as minus zero
        temperature = '0°C'
    return temperature


def parse_wind(wind_speed: str) -> str:
    match wind_speed[0]:
        case "↑":
            wind_speed = f'North at {wind_speed[1:]}'
        case "↗":
            wind_speed = f'North-east at {wind_speed[1:]}'
        case "→":
            wind_speed = f'East at {wind_speed[1:]}'
        case "↘":
            wind_speed = f'South-east at {wind_speed[1:]}'
        case "↓":
            wind_speed = f'South at {wind_speed[1:]}'
        case "↙":
            wind_speed = f'South-west at {wind_speed[1:]}'
        case "←":
            wind_speed = f'West at {wind_speed[1:]}'
        case "↖":
            wind_speed = f'North-west at {wind_speed[1:]}'
        case _:
            print("It shouldn't happened - en.wttr.in has passed unsupported case - ", wind_speed[0])
            sys.exit(1)
    return wind_speed

def parse_location(location: str) -> str:
    location = location.replace('+' ,' ')
    location = location.capitalize()
    return location

# Define print functions for Conky
def print_location():
    print(parse_location(LOCATION))

def print_conditions():
    print(conditions)

def print_precipitation():
    print(precipitation)

def print_pressure():
    print(pressure)

def print_humidity():
    print(humidity)

def print_wind():
    print(parse_wind(wind))

def print_temp():
    print(parse_temp(temp))

def print_feel():
    print(parse_temp(feel))

def print_sunrise():
    print(sunrise)

def print_sunset():
    print(sunset)

def print_update_time():
    print(update_time)


if __name__ == '__main__':
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2] = function args : (*unpacked)
    globals()[args[1]](*args[2:])
