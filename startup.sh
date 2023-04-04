#!/bin/bash

# [ Conky startup script ]
echo 'starting Conky...'
sleep 1
conky -c ~/.config/conky/conkula/conky_config/conky_clock.lua > /dev/null
echo 'Clock is up...'
sleep 1
conky -c ~/.config/conky/conkula/conky_config/conky_weather.lua > /dev/null
echo 'Weather info is up...'
sleep 1
conky -c ~/.config/conky/conkula/conky_config/conky_system.lua > /dev/null
echo 'System info is up...'
sleep 1
conky -c ~/.config/conky/conkula/conky_config/conky_spotify.lua > /dev/null
echo 'Spotify info is up...'
sleep 1
exit
