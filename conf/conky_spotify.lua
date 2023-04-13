conf_dir = os.getenv('HOME') .. '/.config/conky/conkula/conf'
dofile(conf_dir .. '/config_helper.lua')

-- prepare the config
main = conf_main()
spotify = conf_spotify()
conky.config = merge(conky.config, main)
conky.config = merge(conky.config, spotify)

conky.text = [[
${if_running spotify}\
${font1}${color1}${exec ~/.config/conky/conkula/scripts/spotify_artist.sh}
${voffset -14}${alignr}${font2}${color0}${exec ~/.config/conky/conkula/scripts/spotify_title.sh}
${voffset 4}${font5}${color1}${exec ~/.config/conky/conkula/scripts/spotify_status.sh} \
${voffset 2}${alignr}${color0}${execbar 5,200 ~/.config/conky/conkula/scripts/spotify_playback_progress.sh}
${endif}\
]]
