import os
import time
import sys
import glob
from subprocess import run


possible_colors = {'white': 'f8f8f2',
               'red': 'ff5555',
               'yellow': 'f1fa8c',
               'cyan': '8be9fd',
               'orange': 'ffb86c',
               'purple': 'bd93f9',
               'pink': 'ff79c6',
               'lime': '50fa7b'}

def colors():
    print(', '.join(list(possible_colors)))

def setup(*args):
    if len(args) >= 4:
        print('Error: too many arguments provided. \nTry `python3 conkula.py setup main_color accent_color city`')
        return 1
    try:
        main_color = args[0]
        accent_color = args[1]
        if main_color not in list(possible_colors) or accent_color not in list(possible_colors):
            print('Error: invalid color selected. \nTry `python3 conkula.py colors` to see a list of possible colors')
            return 1
        city = args[2]
        print(f'main_color: {main_color}')
        print(f'accent_color: {accent_color}')
        print(f'city: {city}')
        confirm = input('is your configuration correct? type `y` to proceed >>> ')
        if confirm != 'y':
            print('Error: please enter a correct location. \nTry `warsaw` or `los+angeles`')
            return 1
        else:
            run_setup(main_color, accent_color, city)
    except IndexError:
        print('Error: not enough arguments provided. \nTry `python3 conkula.py setup main_color accent_color city`')
    
def run_setup(main_color, accent_color, city):
    set_colors(main_color, accent_color)
    set_city(city)
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
    print(f'Setting the font to {font}')
    # if font...
    time.sleep(1)
    files = glob.glob(f'/home/{os.getlogin()}/.config/conky/conkula/conky_config/conky_*')
    for file in files:
        with open(file, 'r') as f:
            data = f.read()
        data = data.replace('FONT', font)
        with open(file, 'w') as f:
            f.write(data)
    print('set!')

def set_city(city):
    print(f'Setting city to {city.replace("+", " ")}')
    time.sleep(1)
    file = f'/home/{os.getlogin()}/.config/conky/conkula/python/wttr.py'
    with open(file, 'r') as f:
        data = f.read()
    data = data.replace('__LOCATION__', city)
    with open(file, 'w') as f:
        f.write(data)
    print('City set!')
    time.sleep(0.5)

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
        print('Type `sh ~/.config/conky/conkula/startup.sh` to run conky if you change your mind!')

if __name__ == '__main__':
    args = sys.argv
    globals()[args[1]](*args[2:])
