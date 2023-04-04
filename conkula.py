import os
import time
import sys
import glob
from subprocess import run


cwd = os.getcwd()
print(cwd)


colors_list = ['white', 'red', 'yellow', 'cyan', 'orange', 'purple', 'pink', 'lime']
colors_dict = {'white': 'f8f8f2',
               'red': 'ff5555',
               'yellow': 'f1fa8c',
               'cyan': '8be9fd',
               'orange': 'ffb86c',
               'purple': 'bd93f9',
               'pink': 'ff79c6',
               'lime': '50fa7b'}

def colors():
    print(colors_list)

def install(*args):
    if len(args) >= 4:
        print('Error: too many arguments provided, try `python3 conkula.py install main_color accent_color city`')
        return 1
    try:
        main_color = args[0]
        accent_color = args[1]
        if main_color not in colors_list:
            print('Error: invalid accent_color selected. try `python3 conkula.py show_colors` to see a list of possible colors')
            return 1
        if accent_color not in colors_list:
            print('Error: invalid accent_color selected. try `python3 conkula.py show_colors` to see a list of possible colors')
            return 1
        city = args[2]
        print(f'main_color: {main_color}')
        print(f'accent_color: {accent_color}')
        print(f'city: {city}')
        confirm = input('is your configuration correct? type `y` to proceed >>> ')
        if confirm != 'y':
            print('Error: please enter a correct location. try `warsaw` or `los+angeles`')
            return 1
        else:
            set_colors(main_color, accent_color)
            set_city(city)
            initial_run()
    except IndexError:
        print('Error: not enough arguments provided, try `python3 conkula.py install main_color accent_color city`')
    
def set_colors(main_color, accent_color):
    print('setting colors...')
    time.sleep(2)
    files = glob.glob(f'{cwd}/conky_config/conky_*')
    for file in files:
        with open(file, 'r') as f:
            data = f.read()
        data = data.replace('__MAIN_COLOR__', colors_dict[main_color])
        data = data.replace('__ACCENT_COLOR__', colors_dict[accent_color])
        with open(file, 'w') as f:
            f.write(data)
    print('set!')

def set_city(city):
    print('setting city...')
    time.sleep(2)
    file = f'{cwd}/python/wttr.py'
    with open(file, 'r') as f:
        data = f.read()
    data = data.replace('__LOCATION__', city)
    with open(file, 'w') as f:
        f.write(data)
    print('set!')

def initial_run():
    first_run = input('would you like to run conky now? type `y` to run, `n` to skip')
    if first_run == 'y':
        time.sleep(1)
        run('sh ~/.config/conky/conkula/startup.sh', shell=True, check=True, text=True)
    elif first_run == 'n':
        print('type `sh ~/.config/conky/conkula/startup.sh` to run conky if you change your mind')

if __name__ == '__main__':
    args = sys.argv
    globals()[args[1]](*args[2:])
