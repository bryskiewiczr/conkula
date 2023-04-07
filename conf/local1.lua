function cnf ()
    local_config = {
        -- borders
        border_width = 1,
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
        -- user colors
        color0 = '50fa7b', -- ACCENT COLOR
        color1 = 'f8f8f2', -- MAIN COLOR
    }
    return local_config
end