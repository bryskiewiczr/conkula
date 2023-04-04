#!/bin/bash
 
progress=`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Position' | tail -1`
progress=`echo $progress | awk '{print $NF}'`
length=`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'|grep -E -A 1 "length"|grep -E -v "length"|cut -b 43-|cut -d '"' -f 1|grep -E -v ^$`

echo "scale=2 ; ($progress / $length) * 100" | bc
