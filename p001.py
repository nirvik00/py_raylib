from pyray import *
from raylib import *
import time
from os.path import join

init_window(1920, 1080, 'Base')

# import font
x = join('assets', 'spaceship.png')
print(x)
spaceship_texture = load_texture(x)
spaceship_image = load_image(join('assets', 'spaceship.png'))
image_color_grayscale(spaceship_image)
spaceship_new_texture = load_texture_from_image(spaceship_image)

cowboy_image=load_image(join("assets", "animation", "0.png"))
cowboy_texture = load_texture_from_image(cowboy_image)

# import font
font = load_font(join('assets', 'Zero Hour.otf'))

def draw_things():
    draw_pixel(100,200, BLACK)
    draw_circle(1000,500,10,BLACK)
    draw_texture(spaceship_texture, 100,100, WHITE)
    draw_texture_v(spaceship_new_texture, Vector2(200,100), WHITE)
    draw_line_ex(Vector2(0,0), Vector2(1000,1000), 10, WHITE)
    draw_texture(cowboy_texture, 500,500,WHITE)
    draw_text("some text", 10, 400, 50, WHITE)
    draw_text_ex(font, "new text", Vector2(10, 500), 50, 0,  WHITE)

while not window_should_close():
    begin_drawing()
    #
    clear_background(Color(0,0,0,255))
    #
    draw_things()
    #
    end_drawing()

close_window()