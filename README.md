### Dependencies

- [Conky](https://github.com/brndnmtthws/conky) -- v.1.10 or higher due to new Lua syntax
- [PyCurl](http://pycurl.io/)
- __FONT__ font -- to be changed as this is not an open source font

### Setup

1. Create config directory for Conky
    ```
    mkdir -rp ~/.config/conky/
    ```
2. Clone the repository into config directory and cd 
    ```
    git clone https://github.com/bryskiewiczr/conkula.git ~/.config/conky/ & cd ~/.config/conky/conkula
    ```
3. Choose your settings
    ```
    # List of available colors:
    ['white', 'red', 'yellow', 'cyan', 'orange', 'purple', 'pink', 'lime']

    # List of available colors can also be viewed by running
    python3 conkula.py colors
    > ['white', 'red', 'yellow', 'cyan', 'orange', 'purple', 'pink', 'lime']

    # If your city name has more than one word use spaces or + signs to separate the words
    Los Angeles -> los angeles
    or
    Los Angeles -> los+angeles
    ```

4. Start the setup script
    ```
    python3 conkula.py install main_color accent_color city

    i.e. python3 conkula.py install white lime warsaw
    ```

### Running

1. After the installation is done, the program will ask whether or not you wanna run Conky with your new settings

2. Conkula can also be ran manually by invoking
    ```
    bash ~/.config/conky/conkula/startup.sh
    ```

3. Useful aliases to add to your `.bashrc` or `.bash_aliases` file
    ```
    alias conkula="bash ~/.config/conky/conkula/startup.sh"                         # Starts up Conky with this config
    alias conkill="ps aux | grep -ie conky | awk '{print $2}' | xargs kill -9"      # Kills all Conky processes
    ```
### Screenshots

### To-dos

monospace/non-monospace font
additional fonts
