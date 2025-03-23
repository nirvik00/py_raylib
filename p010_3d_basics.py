from pyray import *
from raylib import *


init_window(1000, 700, 'p010 3d basics')

# camera
camera = Camera3D()
camera.position = Vector3(0, 5.0, 5.0)
camera.target = Vector3(0,0,0)
camera.up = Vector3(0,1,0)
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE

# models
# mesh = gen_mesh_cube(1,1,1)
mesh = gen_mesh_cylinder(1,2,32)
model = load_model_from_mesh(mesh)
image = gen_image_gradient_linear(20,20,1,RED, YELLOW)
texture = load_texture_from_image(image)
set_material_texture(model.materials[0], MATERIAL_MAP_ALBEDO, texture)

# move
pos = Vector3()
rotation =0

while not window_should_close():
    dt = get_frame_time()
    # pos.z += 2 * dt 
    rotation += dt
    model.transform = matrix_rotate_x(rotation)

    #
    begin_drawing()
    clear_background(WHITE)
    begin_mode_3d(camera)
    
    #
    draw_grid(10,0.5)
    draw_model(model, pos, 1, WHITE)
    # draw_model_wires(model, Vector3(), 1, RED)
    draw_line_3d(Vector3(-4,0,-2), Vector3(5,2,3), BLACK)

    #
    end_mode_3d()
    end_drawing()

close_window()