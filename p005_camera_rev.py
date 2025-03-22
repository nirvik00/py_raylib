from pyray import *
from raylib import *
import random

Circles=[(Vector2(random.randint(-1000, 1000), random.randint(-1000, 1000)), 
              random.randint(20,50), 
              random.choice([RED, GREEN, YELLOW, BLUE, ORANGE])
              )
              for i in range(100)
              ]

def draw_my_circles():
    for e in Circles:
        draw_circle_v(*e)


init_window(1000, 700, 'p005 rev camera')

player_pos = Vector2(0,0)
player_speed = 400
player_dir = Vector2(0,0)

camera = Camera2D()
camera.zoom = 1
camera.target = player_pos
camera.offset = Vector2(500, 350)

while not window_should_close():
    draw_text("camera", 10,10,20,BLACK)
    fps = get_frame_time()

    #
    player_dir.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT)) 
    player_dir.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))    
    player_pos.x += player_dir.x * fps * player_speed
    player_pos.y += player_dir.y * fps * player_speed
    print(player_pos.x, player_pos.y)
    #
    camera.zoom=1
    camera.target = player_pos

    #
    begin_drawing()
    begin_mode_2d(camera)
    #
    clear_background(WHITE)
    draw_my_circles()
    draw_rectangle_v(player_pos, Vector2(40, 40), BLACK)
    #
    end_mode_2d()
    end_drawing()
    

close_window()