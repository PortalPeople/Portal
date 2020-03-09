def init():
    global frame_num
    global frame_dir
    global current_hue
    global target_hue
    global hue_shift_per_frame

    frame_num = 0
    frame_dir = 1
    current_hue = 120
    target_hue = 120
    hue_shift_per_frame = 3

    