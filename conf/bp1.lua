function cnf_bp ()
    local_config = {
        -- main
        background = false,
        cpu_avg_samples = 2,
        double_buffer = true,
        net_avg_samples = 2,
        no_buffers = true,
        update_interval = 1,
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
        maximum_width = 300,
    }
    return local_config
end
