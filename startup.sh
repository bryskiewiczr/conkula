#!/usr/bin/env bash

trap exit_trap EXIT
set -e

exit_trap () {
  local lc="$BASH_COMMAND" rc=$?
  if [ $rc -ne 0 ]; then
    echo -e "\nCommand \033[1m[$lc]\033[0m exited with code [$rc]\n
            To debug try to execute this command by yourself \033[4mwithout\033[0m '-q' flag"
  fi
}

if pgrep -x conky > /dev/null
then
  echo '\n[!] Killing old Conky processes...'
  killall conky
fi
sleep 0.5

echo '\n[*] Starting Conky...'
sleep 1.5
conky -qc ~/.config/conky/conkula/conf/conky_clock.lua
echo '\t[*] Clock is up!'
sleep 0.5
conky -qc ~/.config/conky/conkula/conf/conky_weather.lua
echo '\t[*] Weather info is up!'
sleep 0.5
conky -qc ~/.config/conky/conkula/conf/conky_system.lua
echo '\t[*] System info is up!'
sleep 0.5
conky -qc ~/.config/conky/conkula/conf/conky_spotify.lua
echo '\t[*] Spotify info is up!'
