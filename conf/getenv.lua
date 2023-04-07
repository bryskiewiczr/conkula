function file_exists(file)
    local f = io.open(file, 'rb')
    if f then f:close() end
    return f ~= nil
end


function lines_from(file)
    if not file_exists(file) then return {} end
    local lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

local home = os.getenv("HOME")
local envpath = '/.config/conky/conkula/python/'
local envfile = home .. envpath .. 'env'
local lines = lines_from(envfile)

-- for k,v in pairs(lines) do
--     if v:find('MAIN') ~= nil then
--         local t = {}
--         for s in string.gmatch(v, '([^' .. '%s' .. ']+)') do
--             table.insert(t, s)
--         end
--         print(t[#t])
--         print(v)
--     end
-- end

function get_color(color)
    local home = os.getenv("HOME")
    local envpath = '/.config/conky/conkula/python/'
    local envfile = home .. envpath .. 'env'
    local lines = lines_from(envfile)
    for k,v in pairs(lines) do
        if v:find(color) ~= nil then
            local t = {}
            for s in string.gmatch(v, '([^' .. '%s' .. ']+)') do
                table.insert(t, s)
            end
            return t[#t]
        end
    end
end

print(get_color('ACCENT'))