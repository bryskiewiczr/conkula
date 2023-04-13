conf_dir = os.getenv('HOME') .. '/.config/conky/conkula/conf'
dofile(conf_dir .. '/config_helper.lua')

-- prepare the config
main = conf_main()
weather = conf_weather()
icon_flag = weather_icons()
conky.config = merge(conky.config, main)
conky.config = merge(conky.config, weather)

if icon_flag == 'false' then
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
else
conky.text = [[
${voffset -20}
${color1}${font9}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_conditions}
${voffset -190}${alignr}${font0}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_temp}
${voffset -35}${alignr}${font2}(${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_feel})
${alignr}${font2}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_location}

${voffset -10}
${color1}${font6} ${font2}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_sunrise} \
${alignr}${color1}${font6} ${font2}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_precipitation}
${color1}${font6} ${font2}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_sunset} \
${alignr}${color1}${font6} ${font2}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_humidity}
${alignr}${color1}${font6} ${font2}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_wind}
${alignr}${color1}${font6} ${font2}${color0}${texeci 1800 python3 ~/.config/conky/conkula/python/wttr.py print_pressure}
]]
end