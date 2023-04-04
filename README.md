### Dependencies:

- [Conky](https://github.com/brndnmtthws/conky) -- v.1.10 or higher due to new Lua syntax
- [PyCurl](http://pycurl.io/)
- Product Sans font -- to be changed as this is not an open source font

### Installation:

- Create config directory for Conky
    ```
    mkdir -rp ~/.config/conky/
    ```
- Clone the repository into config directory 
    ```
    git clone https://github.com/bryskiewiczr/conkula.git ~/.config/conky/
    ```
- Run the installation script 
    ```
    python3 ~/.config/conky/conkula/conkula.py install main_color accent_color city

    # List of available colors:
    ['white', 'red', 'yellow', 'cyan', 'orange', 'purple', 'pink', 'lime']

    # List of available colors can also be viewed by running
    python3 ~/.config/conky/conkula/conkula.py colors
    ``` 

- After the installation is done, the program will ask whether or not you wanna run Conky with your new settings. Conkula can also be ran manually by invoking
    ```
    bash ~/.config/conky/conkula/startup.sh
    ```

### Todo:

monospace/non-monospace font
additional fonts
