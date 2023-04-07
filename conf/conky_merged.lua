-- https://erikflowers.github.io/weather-icons/

conf_dir = os.getenv("HOME") .. '/.config/conky/conkula/conf/'

dofile(conf_dir .. "getcolor.lua")
getc = getc()
getctwo = getctwo()

dofile(conf_dir .. "getenv.lua")
main = get_color('MAIN')
accent = get_color('ACCENT')

conky.config = {
    position = top_right,
    color5 = main,
    color6 = accent,
    font = 'Mono:regular:size=12',
};

function merge(a, b)
    if type(a) == 'table' and type(b) == 'table'
    then
	for k,v in pairs(b)
	do
		if type(v)=='table' and type(a[k] or false)=='table'
		then
			merge(a[k],v)
		else
			a[k]=v
		end
	end
    end
    return a
end

dofile(conf_dir .. "local1.lua")
dofile(conf_dir .. "bp1.lua")
config_local = cnf()
config_bp = cnf_bp()
conky.config = merge( conky.config, config_local )
conky.config = merge( conky.config, config_bp )


conky.text = [[
    ${color5} dynamically loaded main color
    ${color6} dynamically loaded accent color
]];