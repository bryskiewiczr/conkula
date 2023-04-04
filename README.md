### Dependencies

- [Conky](https://github.com/brndnmtthws/conky) -- v.1.10 or higher due to new Lua syntax. Try `conky --version` to see what version is currently installed on your System
- [PyCurl](http://pycurl.io/) -- `pip3 install pycurl`
- One of the currently supported fonts installed on your System. Conkula requires `Regular` and `Bold` font faces:
    - [Lato](https://fonts.google.com/?query=Lato)
    - [Roboto](https://fonts.google.com/?query=Roboto)
    - [Fira Code](https://fonts.google.com/?query=Fira+Code)
    - Mono (*default monospace font)

### Preparation

- Before installing the config on your System please review your configuration options:
    - Possible colors (you can also run `python3 conkula.py colors` to view available colors)
        - `White` (recommended as main color)
        - `Red`
        - `Yellow`
        - `Cyan`
        - `Orange`
        - `Purple`
        - `Pink`
        - `Lime`
    - Possible fonts (must install the font on your System first, you can also run `python3 conkula.py fonts` to view available fonts):
        - `Lato` - Lato font
        - `Roboto` - Roboto font
        - `Fira` - Fira Code font (monospace)
        - `Empty/Mono` - Mono is default if no choice is made or you explicitly type `Mono`, monospace)
    - City for the weather .lua to work
        - If your city's name is single word, simply type the city name, i.e. `warsaw`
        - If your city's name has multiple words, use + signs instead of spaces, i.e. `new+york`

### Setup

1. Create config directory for Conky

    ```
    mkdir -p ~/.config/conky/conkula && cd ~/.config/conky/conkula
    ```

2. Clone the repository into config directory and cd 

    ```
    git clone https://github.com/bryskiewiczr/conkula.git .
    ```

3. Start the setup script

    ```
    python3 conkula.py setup main_color accent_color city font
    ```

    Examples:

    ```
    # set white and lime color scheme with Fira Code font 
    # and Warsaw as the city for your weather widget
    python3 conkula.py setup white lime warsaw fira

    # skip the font to default to Mono
    python3 conkula.py setup white red los+angeles
    ```

### Running

After the installation is done, the program will ask whether or not you wanna run Conky with your new settings

Conkula can also be ran manually by invoking

```
bash ~/.config/conky/conkula/startup.sh
```

### Other

Useful aliases/commands to add to your `.bashrc` or `.bash_aliases` file

```
# Starts up Conky with Conkula config
alias conkula="bash ~/.config/conky/conkula/startup.sh"

# Kills all Conky processes
alias conkill="ps aux | grep -ie conky | awk '{print $2}' | xargs kill -9"

# Also kills all Conky processes, simpler
killall conky
```
### Screenshots

White and Lime setup with Fira Code font

![White and Lime setup with Fira Code font](/screenshots/conkula_white_lime_fira_code.png?raw=true)

White and Purple setup with Lato font

![White and Purple setup with Lato font](/screenshots/conkula_white_purple_lato.png?raw=true)

Yellow and white setup with Roboto font

![Yellow and white setup with Roboto font](/screenshots/conkula_yellow_white_roboto.png?raw=true)

### To-dos

Add support for 12-hour clock format
Selector for position (top-left/top-right), now only defaults to top-right