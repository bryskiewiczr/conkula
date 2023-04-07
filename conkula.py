#!/usr/bin/env python3

import os
import time
import sys
import glob
from subprocess import run


possible_colors = {
    'white': 'f8f8f2',
    'red': 'ff5555',
    'yellow': 'f1fa8c',
    'cyan': '8be9fd',
    'orange': 'ffb86c',
    'purple': 'bd93f9',
    'pink': 'ff79c6',
    'lime': '50fa7b'
}

possible_fonts = {
    'lato': 'Lato',
    'roboto': 'Roboto',
    'fira': 'Fira Code',
    'mono': 'Mono'
}

env_file = f'/home/{os.getlogin()}/.config/conky/conkula/python/env'


def colors():
    print(', '.join(list(possible_colors)))


def fonts():
    print(', '.join(list(possible_fonts)))


def setup(*args):
    if len(args) >= 5:
        print('Error: too many arguments provided. \nTry `python3 conkula.py setup main_color accent_color city font`')
        sys.exit(1)
    try:
        main_color = args[0]
        accent_color = args[1]
        city = args[2]
        try:
            font = args[3]
        except IndexError:
            font = 'Mono'
        if main_color not in list(possible_colors) or accent_color not in list(possible_colors):
            print('Error: invalid color selected. \nTry `python3 conkula.py colors` to see a list of possible colors')
            sys.exit(1)
        print(f'Main color: {main_color} | Accent color: {accent_color} | Font: {font} | City: {city}')
        confirm = input('is your configuration correct? type `y` to proceed >>> ')
        if confirm != 'y':
            print('Error: you didn\'t confirm. \nAborting...')
            sys.exit(1)
        else:
            run_setup(main_color, accent_color, city, font)
    except IndexError:
        print('Error: not enough arguments provided. \nTry `python3 conkula.py setup main_color accent_color city font`')
    

def run_setup(main_color, accent_color, city, font):
    create_env(env_file)
    set_font(font)
    set_colors(main_color, accent_color)
    set_city(city, env_file)
    initial_run()


def set_colors(main_color, accent_color):
    print('Setting colors...')
    time.sleep(1)
    print(f'Setting main color to {main_color}')
    time.sleep(1)
    print(f'Setting accent color to {accent_color}')
    time.sleep(1)
    files = glob.glob(f'/home/{os.getlogin()}/.config/conky/conkula/conky_config/conky_*')
    for file in files:
        with open(file, 'r') as f:
            data = f.read()
        data = data.replace('__MAIN_COLOR__', possible_colors[main_color])
        data = data.replace('__ACCENT_COLOR__', possible_colors[accent_color])
        with open(file, 'w') as f:
            f.write(data)
    print('Colors set!')
    time.sleep(0.5)


def set_font(font):
    match font.casefold():
        case "mono":
            print('Font not selected, defaulting to Mono')
        case "roboto":
            font = possible_fonts[font]
        case "lato":
            font = possible_fonts[font]
        case "fira":
            font = possible_fonts[font]
        case _:
            print('Unsupported font selected, aborting.')
            sys.exit(1)
    print(f'Setting the font to {font}')
    time.sleep(1)
    files = glob.glob(f'/home/{os.getlogin()}/.config/conky/conkula/conky_config/conky_*')
    for file in files:
        with open(file, 'r') as f:
            data = f.read()
        data = data.replace('__FONT__', font)
        with open(file, 'w') as f:
            f.write(data)
    print('Font set!')
    time.sleep(0.5)


def set_city(city, env_file):
    print(f'Setting city to {city.replace("+", " ")}')
    time.sleep(1)
    with open(env_file, 'a') as file_object:
        file_object.write("\nLOCATION = {}".format(city))
    print('City set!')
    time.sleep(0.5)


def create_env(file):
    try:
        # Clear old env file if exists
        with open(file, 'w'): pass
        # Append [vars] block
        with open(file, 'a') as file_object:
            file_object.write("[vars]")
    except OSError as e:
        print('Failed creating the env file.')
        print(e)
        sys.exit(1)


def initial_run():
    first_run = input('Would you like to run conky now? \n(y/n) >>> ')
    if first_run == 'y'.casefold():
        print('Here we go!')
        time.sleep(1)
        command = 'sh ~/.config/conky/conkula/startup.sh'
        print(f'Executing {command}')
        run(f'{command}', shell=True, check=True, text=True)
    else:
        print('Skipping the startup')
        print('Type `bash ~/.config/conky/conkula/startup.sh` to run conky if you change your mind!')


if __name__ == '__main__':
    args = sys.argv
    try:
        globals()[args[1]](*args[2:])
    except KeyError:
        print('Error: invalid command\nHave you missed the `setup` keyword?')
        print(f'Try: `python3 conkula.py setup main_color accent_color city font`')
