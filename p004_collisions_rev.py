from pyray import *
from raylib import *

init_window(1000, 700, "base")

r1 = Rectangle(100,100,100, 100)
r2 = Rectangle(100,100,100, 100)

while not window_should_close():
    mos = get_mouse_position()

    r1.x = mos.x
    r1.y = mos.y

    begin_drawing()
    clear_background(BLACK)

    draw_rectangle_rec(r2, RED)
    draw_rectangle_rec(r1, WHITE)

    x = get_collision_rec(r1, r2)
    draw_rectangle_rec(x, GREEN)



    end_drawing()

close_window()