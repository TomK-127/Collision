import numpy.random as rd
import numpy as np
from display import *
from solver import *

def init_list(N):
    balls = []
    r = 10.
    v = 10.
    x = 400./float(N+1)
    for i in range(N):
        m = r*(1.-0.05*i)
        vv = [-1.*v, 1.*v]
        vx = [float(i+1)*x, float(i+1)*x]
        balls.append(Ball(m, m, vx, vv))
    return balls


def init_grid(N, size):
    bounds_sep = 50

    grid_size = np.sqrt(N).astype(int)
    start = np.linspace(bounds_sep, (size - bounds_sep), grid_size)

    # Position
    # [<atom i>, <x=0,y=1>]
    pos = np.zeros([N, 2])
    row = 0
    for i in range(0, N, grid_size):
        pos[i:(i + grid_size), 0] = start
        pos[i:(i + grid_size), 1] = start[row]
        row += 1

    # Velocity
    vel_scale = 30
    vel = np.zeros([N, 2])
    vel[:, 0] = (np.random.rand(N) - 0.5) * vel_scale
    vel[:, 1] = (np.random.rand(N) - 0.5) * vel_scale

    ball = []
    mass = 5
    radius = 15
    for i in range(N):
        ball.append(solver.Ball(mass, radius, pos[i], vel[i]))
    return ball

if __name__ == "__main__":
    size = 400.
    N = 25
    balls = init_grid(N, size)
    step = 0.02
    Display(balls, step, size)



