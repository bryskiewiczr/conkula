conf_dir = os.getenv('HOME') .. '/.config/conky/conkula/conf'
env_file = os.getenv('HOME') .. '/.config/conky/conkula/python/env'

function file_exists(file)
    local f = io.open(file, 'rb')
    if f then f:close() end
    return f ~= nil
end

function read_file(file)
    if not file_exists(file) then return {} end
    local lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

function ltrim(string)
    return string:match('^%s*(.*)')
end

function get_env(var)
    local lines = read_file(env_file)
    for k, v in pairs(lines) do
        if v:find(var) ~= nil then
            local t = {}
            for s in string.gmatch(v, '([^' .. '=' .. ']+)') do
                table.insert(t, ltrim(s))
            end
            return t[#t]
        end
    end
end
