from pyray import *
from raylib import *

init_window(1000, 700, "test_collisions")
player_pos = Vector2(0,0)
obstacle_pos = Vector2(500, 400)
player_radius = 50
obstacle_radius = 30

r1 = Rectangle(0,0,100,200)
r2 = Rectangle(500, 200, 100, 100)
while not window_should_close():
    # input
    player_pos = get_mouse_position()

    #########   collision
    # x = check_collision_circles(player_pos, player_radius, obstacle_pos, obstacle_radius)
    # if is_mouse_button_pressed(0):
    #     print(f'circle collision {x}')

    collision_rect_circle = check_collision_circle_rec(obstacle_pos, obstacle_radius, r1)
    collision_rect = check_collision_recs(r1, r2)
    if is_mouse_button_pressed(0):
        print(f'circle-rect collision {collision_rect_circle}')
        print(f'rect-rect collision {collision_rect}')


    begin_drawing()
    clear_background(BLACK)
    # draw_circle_v(player_pos, player_radius, WHITE)
    draw_circle_v(obstacle_pos, obstacle_radius, RED)

    mos = get_mouse_position()
    r1.x = mos.x
    r1.y = mos.y
    draw_rectangle_rec(r1, WHITE)
    draw_rectangle_rec(r2, BLUE)
    if collision_rect:
        overlap_rect = get_collision_rec(r1, r2)
        if overlap_rect:
            draw_rectangle_rec(overlap_rect, GREEN)

    end_drawing()

close_window()