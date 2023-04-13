#!/usr/bin/env python3

import os
import time
import sys
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
    print('[*] Available colors:')
    for color in possible_colors:
        print(f'\t[-] {color}')


def fonts():
    print('[*] Available fonts:')
    for font in possible_fonts:
        print(f'\t[-] {font}\t-> {possible_fonts[font]}')


def setup(*args):
    if len(args) >= 6:
        print('\033[91m[!] Error: too many arguments provided.')
        print('\033[0;36m[*] Try: `python3 conkula.py setup main_color accent_color city weather_icons font`')
        sys.exit(1)
    try:
        main_color = args[0].casefold()
        accent_color = args[1].casefold()
        city = args[2].casefold()
        icons = args[3].casefold()
        if icons in ['icons', 'text']:
            pass
        else:
            print(f'\033[91m[!] Error: incorrect argument passed for `icons`.')
            print('\033[0;36m[*] Try: `icons` or `text`')
            sys.exit(1)
        try:
            font = args[4].casefold()
        except IndexError:
            font = 'mono'
    except IndexError:
        print('\033[91m[!] Error: not enough arguments provided.')
        print('\033[0;36m[*] Try: `python3 conkula.py setup main_color accent_color city weather_icons font`')
        sys.exit(1)
    if main_color not in list(possible_colors) or accent_color not in list(possible_colors):
        print('\033[91m[!] Error: invalid color selected.')
        print('\033[0;36m[*] Try `python3 conkula.py colors` to see a list of possible colors')
        sys.exit(1)
    if font.casefold() not in list(possible_fonts):
        print('\033[91m[!] Error: invalid font selected.')
        print('\033[0;36m[*] Try `python3 conkula.py fonts` to see a list of possible fonts')
        sys.exit(1)
    print(f'[*] Configuration:')
    print(f'\t[-] Main Color: {main_color}\n\t[-] Accent Color: {accent_color}\n\t[-] City: {city}\n\t[-] Weather: {icons}\n\t[-] Font: {font}\n')
    confirm = input('[>] Is your configuration correct?: ')
    if confirm != 'y':
        print('\033[91m[!] Error: you didn\'t confirm. Aborting...')
        sys.exit(1)
    else:
        run_setup(main_color, accent_color, city, font, icons)
    

def run_setup(main_color, accent_color, city, font, icons):
    create_env(env_file)
    set_font(font, env_file)
    set_colors(main_color, accent_color, env_file)
    set_city(city, env_file)
    set_icons(icons, env_file)
    initial_run()


def set_city(city, env_file):
    print(f'\n[*] Setting city to {city.replace("+", " ")}')
    time.sleep(1)
    with open(env_file, 'a') as f:
        f.write(f'\nLOCATION={city}')
    print('\t[*] City set!')
    time.sleep(0.5)


def set_icons(icons, env_file):
    if icons == 'icons':
        print(f'\n[*] Setting weather to {icons}')
        time.sleep(1)
        with open(env_file, 'a') as f:
            f.write(f'\nWEATHER_ICONS=true')
    elif icons == 'text':
        print(f'\n[*] Settings weather to {icons}')
        time.sleep(1)
        with open(env_file, 'a') as f:
            f.write(f'\nWEATHER_ICONS=false')
    print('\t[*] Weather set!')
    time.sleep(0.5)


def set_colors(main_color, accent_color, env_file):
    print(f'\n[*] Setting main color to {main_color}')
    print(f'[*] Setting accent color to {accent_color}')
    with open(env_file, 'a') as f:
        f.write(f'\nMAIN_COLOR={possible_colors[main_color]}')
        f.write(f'\nACCENT_COLOR={possible_colors[accent_color]}')
    print('\t[*] Colors set!')
    time.sleep(0.5)


def set_font(font, env_file):
    print(f'\n[*] Setting font to {possible_fonts[font]}')
    with open(env_file, 'a') as f:
        f.write(f'\nFONT={possible_fonts[font]}')
    print('\t[*] Font set!')
    time.sleep(0.5)


def create_env(file):
    try:
        # Clear old env file if exists
        with open(file, 'w'): pass
        # Append [vars] block
        with open(file, 'a') as file_object:
            file_object.write("[vars]")
    except OSError as e:
        print('\033[91m[!] Error: failed creating the env file.')
        print(e)
        sys.exit(1)


def initial_run():
    first_run = input('\n[>] Would you like to run conky now?: ')
    if first_run == 'y'.casefold():
        time.sleep(1)
        command = 'sh ~/.config/conky/conkula/startup.sh'
        print(f'\n[*] Here we go! Executing `{command}`')
        run(f'{command}', shell=True, check=True, text=True)
    else:
        print('\n\033[1;33m[!] Skipping the startup.')
        print('\033[0;36m[*] Type: `bash ~/.config/conky/conkula/startup.sh` to run Conky if you change your mind!')


if __name__ == '__main__':
    args = sys.argv
    try:
        globals()[args[1]](*args[2:])
    except KeyError as err:
        print(err)
        print('\033[91m[!] Error: invalid command. Have you missed the `setup` keyword?')
        print(f'\033[0;36m[*] Try: `python3 conkula.py setup main_color accent_color city weather_icons font`')
