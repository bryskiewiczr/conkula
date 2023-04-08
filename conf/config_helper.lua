conf_dir = os.getenv('HOME') .. '/.config/conky/conkula/conf'
dofile(conf_dir .. '/env_parser.lua')

-- function to merge the config tables
function merge(a, b)
    if type(a) == 'table' and type(b) == 'table'
        then
        for k,v in pairs(b)
        do
            if type(v) == 'table' and type(a[k] or false) == 'table'
            then
                merge(a[k], v)
            else
                a[k] = v
            end
        end
    end
    return a
end

-- main config
function conf_main()
    main_config = {
        -- main
        background = true,
        cpu_avg_samples = 2,
        double_buffer = true,
        net_avg_samples = 2,
        no_buffers = true,
        -- outs
        out_to_console = false,
        out_to_ncurses = false,
        out_to_stderr = false,
        out_to_x = true,
        -- window
        own_window = true,
        own_window_transparent = true,
        own_window_argb_visual = true,
        own_window_argb_value = 255,
        own_window_class = 'Conky',
        own_window_type = 'desktop',
        extra_newline = false,
        use_spacer = 'none',
        border_inner_margin = 20,
        border_outer_margin = 0,
        -- borders
        border_width = 0,
        draw_borders = false,
        stippled_borders = 0,
        -- graphs
        show_graph_range = false,
        show_graph_scale = false,
        draw_graph_borders = true,
        -- font
        use_xft = true,
        uppercase = false,
        draw_outline = false,
        draw_shades = false,
        -- default colors
        default_color = 'white',
        default_outline_color = 'black',
        default_shade_color = 'black',
        -- env variables
        color0 = get_env('ACCENT_COLOR'),
        color1 = get_env('MAIN_COLOR'),
        font0 = get_env('FONT') .. ':bold:size=36',
        font1 = get_env('FONT') .. ':bold:size=24',
        font2 = get_env('FONT') .. ':bold:size=12',
        font3 = get_env('FONT') .. ':regular:size=36',
        font4 = get_env('FONT') .. ':regular:size=24',
        font5 = get_env('FONT') .. ':regular:size=12',
    }
    return main_config
end

-- clock config
function conf_clock()
    clock_config = {
        update_interval = 1,
        alignment = 'top_right',
        gap_x = 150,
        gap_y = 150,
        minimum_height = 5,
        minimum_width = 300,
        maximum_width = 300,
    }
    return clock_config
end

-- weather config
function conf_weather()
    weather_config = {
        update_interval = 1,
        alignment = 'top_right',
        gap_x = 150,
        gap_y = 320,
        minimum_height = 5,
        minimum_width = 300,
        maximum_width = 300,
    }
    return weather_config
end

-- system monitor config
function conf_system()
    system_config = {
        update_interval = 1,
        alignment = 'top_right',
        gap_x = 150,
        gap_y = 600,
        minimum_height = 5,
        minimum_width = 300,
        maximum_width = 300,
    }
    return system_config
end

-- spotify monitor config
function conf_spotify()
    system_config = {
        update_interval = 1,
        alignment = 'top_right',
        gap_x = 150,
        gap_y = 845,
        minimum_height = 5,
        minimum_width = 300,
        maximum_width = 300,
    }
    return system_config
end
