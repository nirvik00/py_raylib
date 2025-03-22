from pyray import *
from raylib import *
from os.path import join
import numpy as np

class ship:
    def __init__(self):
        self.screen_cen = Vector2(get_screen_width()/2, get_screen_height()/2)
        self.img= load_image(join("assets", "spaceship.png"))
        self.texture = load_texture_from_image(self.img)
        self.w = self.texture.width
        self.h = self.texture.height
        self.origin = Vector2(self.w/2, self.h/2)
        self.source_rect = [0,0,self.w, self.h]
        self.destination_rect =[get_screen_width()/2, get_screen_height()/2, self.w, self.h]
    
    def rotate(self, mos):
        u = np.array([100, 0])
        v = np.array([mos.x - self.screen_cen.x, mos.y - self.screen_cen.y])
        cos_theta = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
        radians = np.arccos(np.clip(cos_theta, -2*np.pi, 2*np.pi))
        degrees = np.degrees(radians)
        return degrees


init_window(1000,700, "p003 rev")
CEN = Vector2(get_screen_width() /2, get_screen_height()/2)
MOS = CEN

def draw_objects():
    # draw_rectangle(100,100,20,30,WHITE)
    # draw_line_ex(MOS, CEN, 2, WHITE)
    pass

def draw_ship(cen_, mos_):
    s = ship()
    degrees = s.rotate(mos_)
    if mos_.y > cen_.y:
        draw_texture_pro(s.texture, s.source_rect, s.destination_rect, s.origin, degrees + 90, WHITE)
    else:
        draw_texture_pro(s.texture, s.source_rect, s.destination_rect, s.origin, 90 - degrees, WHITE)


while not window_should_close():
    # events
    MOS = get_mouse_position()

    # update

    # draw
    begin_drawing()
    clear_background(BLACK)
    draw_objects()
    draw_ship(CEN, MOS)

    end_drawing()

close_window()