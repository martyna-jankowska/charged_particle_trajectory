import numpy as np


def update_force(q, e, v, b):
    return q * (e + np.cross(v, b))


def update_velocity(v, m, f, t):
    return v + (f / m * t)


def update_position(p, v, f, t, m):
    return p + v * t + 0.5 * (f / m * (t ** 2))


# constants
q = -1.6e-19
m = 9e-31

dt = 0.0000001
num_steps = 1000

E = np.array([0, 1e-1, 1e-6])
B = np.array([0, 1e-7, 1e-5])

# initialize arrays for storing position, force and velocity
vel = np.zeros((num_steps, 3))
pos = np.zeros((num_steps, 3))
force = np.zeros((num_steps, 3))

# set starting conditions
vel[0] = np.array([0, 0, 1e6])
force[0] = update_force(q, E, vel[0], B)

for i in range(1, num_steps):
    pos[i] = update_position(pos[i - 1], vel[i - 1], force[i - 1], dt, m)
    vel[i] = update_velocity(vel[i - 1], m, force[i - 1], dt)
    force[i] = update_force(q, E, vel[i - 1], B)

    # checking for invalid values
    # if np.isnan(pos[i]).any() or np.isinf(pos[i]).any() or np.isnan(vel[i]).any() or np.isinf(vel[i]).any() or np.isnan(
            # force[i]).any() or np.isinf(force[i]).any():
        # break

print(force)
print(vel)
print(pos)
