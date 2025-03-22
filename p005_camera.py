from pyray import *
from raylib import *

from random import randint, choice

init_window(1000, 700, "p005_camera")

pos = Vector2(200,200)
radius = 50
direction = Vector2()
speed = 400

circles = [
    (
        Vector2(randint(-2000, 2000), randint(-1000, 1000)),
        randint(50, 200),
        choice([RED, GREEN, BLUE, YELLOW, ORANGE]),
    )
    for i in range(100)
]

rotate_direction=0
zoom_direction=0
camera = Camera2D()
camera.zoom= 1
camera.target = pos
camera.offset = Vector2(500,350)
# camera.rotation = 45

while not window_should_close():
    # update
    fps = get_frame_time()
    direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
    direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
    direction = vector2_normalize(direction)
    pos.x += direction.x * speed * fps
    pos.y += direction.y * speed * fps

    #
    rotate_direction = int(is_key_down(KEY_D)) - int(is_key_down(KEY_A))
    camera.rotation += rotate_direction * fps *100
    zoom_direction = int(is_key_down(KEY_Q)) - int(is_key_down(KEY_S))
    camera.zoom += zoom_direction *fps * 2
    camera.zoom= max(0.2, camera.zoom)
    camera.zoom = min(5, camera.zoom)
    camera.target = pos


    #
    begin_drawing()
    begin_mode_2d(camera)
    clear_background(WHITE)
    
    for circle in circles:
        draw_circle_v(*circle)

    draw_circle_v(pos, radius, BLACK)
    end_mode_2d()

    draw_text("zoom " + str(camera.zoom), 10,10,20, BLACK)
    draw_text("rotation " + str(camera.rotation), 10,45, 20, BLACK)
    end_drawing()

close_window()