conf_dir = os.getenv('HOME') .. '/.config/conky/conkula/conf'
dofile(conf_dir .. '/config_helper.lua')

-- prepare the config
main = conf_main()
clock = conf_clock()
conky.config = merge(conky.config, main)
conky.config = merge(conky.config, clock)

conky.text = [[
${font0}${color0}${time %H}:${time %M}:${time %S}
${voffset -20}${font1}${color1}${time %d} ${color0}${time %b} ${color1}${time %Y}
${font1}${color1}${time %A}
]];
