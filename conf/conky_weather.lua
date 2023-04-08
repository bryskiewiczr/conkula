conf_dir = os.getenv('HOME') .. '/.config/conky/conkula/conf'
dofile(conf_dir .. '/config_helper.lua')

-- prepare the config
main = conf_main()
weather = conf_weather()
conky.config = merge(conky.config, main)
conky.config = merge(conky.config, weather)

conky.text = [[
${font0}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_temp}
${voffset -20}${font1}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_conditions}
${voffset -10}${font5}${color1}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_location}, \
${font5}${color1}feels like: ${color0}${font2}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_feel}
${font5}${color1}Humidity: ${alignr}${color0}${font2}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_humidity}
${font5}${color1}Precipitation: ${alignr}${color0}${font2}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_precipitation}
${font5}${color1}Wind: ${alignr}${color0}${font2}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_wind}
${font5}${color1}Pressure: ${alignr}${color0}${font2}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_pressure}
${font5}${color1}Updated: ${alignr}${color0}${font2}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_update_time}
]]
