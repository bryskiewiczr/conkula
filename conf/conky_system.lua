conf_dir = os.getenv('HOME') .. '/.config/conky/conkula/conf'
dofile(conf_dir .. '/config_helper.lua')

-- prepare the config
main = conf_main()
system = conf_system()
conky.config = merge(conky.config, main)
conky.config = merge(conky.config, system)

conky.text = [[
${font5}${color1}Host: ${alignr}${color0}${font2}${nodename}
${font5}${color1}Uptime: ${alignr}${color0}${font2}${uptime}
${font5}${color1}CPU: ${alignr}${color0}${font2}${cpu cpu0}%
${alignr}${cpubar 5,200}
${font5}${color1}RAM: ${alignr}${color0}${font2}${memperc}%
${alignr}${membar 5,200}
${font5}${color1}SWAP: ${alignr}${color0}${font2}${swapperc}%
${alignr}${swapbar 5,200}
${font5}${color1}Root: ${alignr}${color0}${font2}${fs_used}/${fs_size /}
${alignr}${fs_bar 5,200 /}
]]
