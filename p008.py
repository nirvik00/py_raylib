from pyray import *
from raylib import *
from os.path import join

level_map = [
    '1111111111111111111',
    '1110000000000000001',
    '1110000000001111111',
    '1110000000000000111',
    '1110000200000000011',
    '1110000000000100001',
    '1110000000000100001',
    '1111100000000100001',
    '1111100000000100001',
    '1111100000000100001',
    '1111111111111111111'
]

def get_blocks(level_map):
    blocks=[]
    for row_index, row in enumerate(level_map):
        for col_index, cell in enumerate(row):
            if cell == '1':
                pos = Vector2(col_index*100, row_index*100)
                block = Block(pos, 0)
                blocks.append(block)
    return blocks


class Sprite:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
    def move(self, dt):
        self.pos.x += self.dir.x * dt * self.speed
        self.pos.y += self.dir.y * dt * self.speed
    def get_rectangle(self):
        return Rectangle(self.pos.x, self.pos.y, self.size.x, self.size.y)
    def get_left_rectangle(self):
        return Rectangle(self.pos.x-10, self.pos.y, self.size.x, self.size.y)
    def get_right_rectangle(self):
        return Rectangle(self.pos.x+10, self.pos.y, self.size.x, self.size.y)
    def get_up_rectangle(self):
        return Rectangle(self.pos.x, self.pos.y-10, self.size.x, self.size.y)
    def get_down_rectangle(self):
        return Rectangle(self.pos.x, self.pos.y+10, self.size.x, self.size.y)
        
class Player(Sprite):
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self.dir = Vector2(0,0)
        self.size = Vector2(50,50)
        self.block_movement = {'up': False, 'down': False, 'left': False, 'right': False}
        self.color= GRAY
    def update(self, dt, blocks):
        self.dir.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        self.dir.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
        self.dir = Vector2Normalize(self.dir)
        for block in blocks:
            b = block.get_rectangle()
            L = self.get_left_rectangle()
            if self.dir.x < 0:
                if check_collision_recs(L, b) == True:
                    return
            R = self.get_right_rectangle()
            if self.dir.x > 0:
                if check_collision_recs(R, b) == True:
                    return
            U = self.get_up_rectangle()
            if self.dir.y < 0:
                if check_collision_recs(U, b) == True:
                    return
            D= self.get_down_rectangle()
            if self.dir.y > 0:
                if check_collision_recs(D, b) == True:
                    return        
        self.move(dt)
    def draw(self):
        draw_rectangle_v(self.pos, self.size, self.color)
        draw_circle_v(self.pos, 10, GREEN)


class Block(Sprite):
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self.size = Vector2(100,100)
        self.color = WHITE
    def draw(self):
        draw_rectangle_v(self.pos, self.size, self.color)

init_window(1920, 1080, 'base')

player = Player(Vector2(400, 540), 500)
blocks = get_blocks(level_map)

while not window_should_close():
    dt = get_frame_time()
    player.update(dt, blocks)

    #
    begin_drawing()
    clear_background(BLACK)

    #
    for block in blocks:
        block.draw()

    #
    player.draw()
    draw_text("blocks: " + str(len(blocks)), 10, 10, 20, RED)

    #
    end_drawing()

close_window()




