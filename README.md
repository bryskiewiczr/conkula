### Dependencies:

- conky v.1.10+ -- due to new Lua syntax
- pycurl
- Product Sans font

### Installation:

- Create config directory for Conky [if not exists] `mkdir -rp ~/.config/conky/`
- Clone the repository into config directory `git clone https://github.com/bryskiewiczr/conkula.git ~/.config/conky/`
- Run the installation script `python3 ~/.config/conky/conkula/conkula.py install main_color accent_color city` 
    - List of available colors: `['white', 'red', 'yellow', 'cyan', 'orange', 'purple', 'pink', 'lime']`
    - List can also be viewed by running `python3 ~/.config/conky/conkula/conkula.py colors`
- After the installation is done, the program will ask whether or not you wanna run Conky with your new settings
- If you skip the above step, you can run the config with `sh ~/.config/conky/conkula/startup.sh`