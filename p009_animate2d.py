from pyray import *
from raylib import *
from os.path import join


init_window(1000, 700, 'p009 animate 2d')

animation_frames = [load_texture(join("assets", "animation", f'{i}.png'))for i in range(7)]
animation_index = 0
animation_speed = 5
while not window_should_close():
    dt = get_frame_time()
    animation_index += 5 * dt
    # animation_index = animation_index % 7
    begin_drawing()
    clear_background(BLACK)
    draw_texture(animation_frames[int(animation_index)%7], 0, 0, WHITE)
    end_drawing()

close_window()