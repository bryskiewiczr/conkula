conky.config = {
    -- main
    background = true,
    cpu_avg_samples = 2,
    double_buffer = true,
    net_avg_samples = 2,
    no_buffers = true,
    update_interval = 1.0,
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
    -- alignment
    alignment = 'top_right',
    gap_x = 150,
    gap_y = 150,
    minimum_height = 5,
    minimum_width = 300,
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
    font = 'mono:regular:size=12',
    draw_outline = false,
    draw_shades = false,
    -- default colors
    default_color = 'white',
    default_outline_color = 'black',
    default_shade_color = 'black',
    -- user colors
    color0 = '__ACCENT_COLOR__', -- ACCENT COLOR
    color1 = '__MAIN_COLOR__', -- MAIN COLOR
}


conky.text = [[
${font __FONT__:bold:size=36}${color0}${time %H}:${time %M}:${time %S}
${voffset -20}${font __FONT__:bold:size=24}${color1}${time %d} ${color0}${time %b} ${color1}${time %Y}
${font __FONT__:bold:size=24}${color1}${time %A}
]]
