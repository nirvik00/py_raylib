import math
import numpy as np

def calc_ang2(u_, v_):
    u = np.array(u_)
    v = np.array(v_)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    cos_theta = np.dot(u, v) / (norm_u * norm_v)
    #print(norm_u, norm_v, cos_theta)
    ang_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    ang_deg = np.degrees(ang_rad)
    print(f"np = {ang_deg}")

def calc_ang(u, v):
    norm_u = math.sqrt((u[0] * u[0]) + (u[1] * u[1]))
    norm_v = math.sqrt((v[0] * v[0]) + (v[1] * v[1]))
    print(norm_u)
    print(norm_v)
    try:
        dp = (u[0] * v[0] + u[1] * v[1]) / (norm_u * norm_v)
    except:
        dp = math.pi/2
    ang = math.acos(dp)
    deg = ang * 180 / math.pi
    print(f"direct calc ang = {deg}")

u = [0,0]
v = [100,100]

calc_ang(u, v)
calc_ang2(u, v)