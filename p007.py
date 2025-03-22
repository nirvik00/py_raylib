from pyray import *
from raylib import *
from os.path import join

class Sprite:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
    def move(self, dt):
        self.pos.x += self.dir.x * self.speed * dt
        self.pos.y += self.dir.y * self.speed * dt

class Player(Sprite):
    def __init__(self, pos):
        super().__init__(pos, speed=400)
        # self.pos = pos
        # self.speed = 400
        self.texture = load_texture(join("assets", "spaceship.png"))
        self.dir = Vector2(0,0)
    def update(self, dt):
        self.dir.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        self.dir.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
        self.dir = Vector2Normalize(self.dir)
        self.move(dt)
    def draw(self):
        draw_texture_v(self.texture, self.pos, WHITE)

class Block(Sprite):
    def __init__(self, pos):
        super().__init__(pos, speed= 40)
        # self.pos = pos
        self.dir = Vector2(1,0)
        self.size = Vector2(100,100)
    def update(self, dt):
        self.move(dt)
    def draw(self):
        draw_rectangle_v(self.pos, self.size, RED)


init_window(1000, 700, 'oop')
player = Player(Vector2(500, 350))
block = Block(Vector2(200,200))
sprites = [player, block]
while not window_should_close():
    #
    #########   update
    dt = get_frame_time()
    for e in sprites:
        e.update(dt)
    #
    #########   drawing
    begin_drawing()
    clear_background(BLACK)
    #
    for e in sprites:
        e.draw()
    #
    end_drawing()

close_window()