from pyray import *
from raylib import *
from os.path import join

init_window(1000, 1000, "p002")
set_target_fps(60)

ship_vel = Vector2(100.0, 100.0)
ship_pos = Vector2(0.0, 0.0)
ship_dir = Vector2(1.0, 1.0)
spaceship_image = load_image(join('assets', 'spaceship.png'))
spaceship_texture = load_texture_from_image(spaceship_image)


while not window_should_close():
    dt = get_frame_time()

    if is_mouse_button_down(0):
        print('left button pressed')
    elif is_mouse_button_down(1):
        print('right button pressed')
    elif is_mouse_button_down(2):
        print('scroll button pressed')
    
    if is_key_down(KEY_W):
        print('w pressed')

    # updates
    if ship_pos.x < 0:
        ship_dir.x = 0
    if ship_pos.y <0 or ship_pos.y + spaceship_texture.height> get_screen_width():
        ship_dir.y *= -1
    ship_pos.x += ship_dir.x * ship_vel.x * dt 
    ship_pos.y += ship_dir.y * ship_vel.y * dt

    # drawing
    begin_drawing()
    clear_background(Color(0,0,0,255))
    draw_texture_v(spaceship_texture, ship_pos, WHITE)
    end_drawing()

close_window()

