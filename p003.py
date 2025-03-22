from pyray import *
from raylib import *
from os.path import join
import math
import numpy as np

init_window(1000,700,'p003')
set_target_fps(60)

ship_image = load_image(join('assets', 'spaceship.png'))
ship_texture = load_texture_from_image(ship_image)
ship_origin = Vector2(ship_texture.width/2, ship_texture.height/2)
ship_source_rect = [0,0,ship_texture.width, ship_texture.height]
ship_dest_rect = [get_screen_width()/2, get_screen_height()/2, ship_texture.width, ship_texture.height]

CEN = ship_dest_rect[:2]

ship_speed= 1000
ship_pos = Vector2(0,0)
ship_dir = Vector2(1,1)
ship_vel = Vector2(1,1)




while not window_should_close():
    if is_key_down(KEY_W):
        ship_vel = Vector2(0, -ship_speed)
    elif is_key_down(KEY_S):
        ship_vel = Vector2(0, ship_speed)
    elif is_key_down(KEY_A):
        ship_vel = Vector2(-ship_speed, 0)
    elif is_key_down(KEY_D):
        ship_vel = Vector2(ship_speed, 0)
    dt = get_frame_time()
    ship_pos.x += ship_dir.x * ship_vel.x * dt
    ship_pos.y += ship_dir.y * ship_vel.y * dt
    if ship_pos.x < 0:
        ship_pos.x=0
    elif ship_pos.x + ship_texture.width > get_screen_width():
        ship_pos.x = get_screen_width() - ship_texture.width
    elif ship_pos.y < 0:
        ship_pos.y=0
    elif ship_pos.y + ship_texture.height > get_screen_height():
        ship_pos.y = get_screen_height() - ship_texture.height

    mos = get_mouse_position()
    u = np.array([100 , 0])
    v = np.array([mos.x - CEN[0], mos.y - CEN[1]])
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    cos_theta = np.dot(u, v) / (norm_u * norm_v)
    ang_rad = np.arccos(np.clip(cos_theta, -2*np.pi, 2*np.pi))
    ang_deg = np.degrees(ang_rad)
    begin_drawing()
    clear_background(BLACK)
    if mos.y>CEN[1]:
        draw_texture_pro(ship_texture, ship_source_rect, ship_dest_rect, ship_origin, ang_deg + 90, WHITE)
    else:
        draw_texture_pro(ship_texture, ship_source_rect, ship_dest_rect, ship_origin, 90 - ang_deg, WHITE)
    draw_line_ex(ship_dest_rect[:2], mos, 2, WHITE)
    end_drawing()

close_window()