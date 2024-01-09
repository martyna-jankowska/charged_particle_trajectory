import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk


def update_force(q, e, v, b):
    return q * (e + np.cross(v, b))


def update_velocity(v, m, f, t):
    return v + (f / m * t)


def update_position(p, v, f, t, m):
    return p + v * t + 0.5 * (f / m * (t ** 2))


# constants
q = -1.6e-19
m = 9e-31

dt = 1e-9
num_steps = 100000

E = np.array([2e-8, 4e-7, 0])
B = np.array([1e-7, 0, 2e-6])

start_vel = np.array([3e9, 1e7, 1e6])
start_force = update_force(q, E, start_vel, B)
start_pos = np.zeros(3)

with open("data.csv", 'w') as data_file:
    data_file.write("x,y,z\n")
    data_file.close()

for i in range(0, num_steps):
    with open("data.csv", "a") as data_file:
        data_file.write(f"{",".join(str(i) for i in start_pos)}\n")
        data_file.close()

    pos = update_position(start_pos, start_vel, start_force, dt, m)
    vel = update_velocity(start_vel, m, start_force, dt)
    start_pos = pos
    start_force = update_force(q, E, start_vel, B)
    start_vel = vel

with open("data.csv", "r") as data_file:
    x, y, z = np.loadtxt(data_file, usecols=(0,  1, 2), delimiter=',', unpack=True, skiprows=1)

ax = plt.figure(figsize=(10, 10)).add_subplot(projection='3d')
ax.plot3D(x, y, z, 'red', label="particle trajectory")
ax.legend()
ax.set_xlabel("x", size=20)
ax.xaxis.set_tick_params(labelsize=14)
ax.set_ylabel("y", size=20)
ax.yaxis.set_tick_params(labelsize=14)
ax.set_zlabel("z", rotation=0, size=20)
ax.zaxis.set_tick_params(labelsize=14)
ax.set_title('Charged Particle Trajectory', size=24)
plt.get_current_fig_manager().set_window_title("Title")
plt.show()

root = Tk()


root.mainloop()


