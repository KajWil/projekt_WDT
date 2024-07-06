import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

# Stałe
s = 10
b = 8/3
r = 28

# Przykładowe wartości początkowe
x0 = 1
y0 = 1
z0 = 1

def uklad(u, t):
    x, y, z = u
    dxdt = s*(y - x)
    dydt = x*(r - z) - y
    dzdt = x*y - b*z
    return [dxdt, dydt, dzdt]

def roz_uklad(x0, y0, z0, t):
    warunki = [x0, y0, z0]
    roz = odeint(uklad, warunki, t)
    x_roz = roz[:, 0]
    y_roz = roz[:, 1]
    z_roz = roz[:, 2]
    return t, x_roz, y_roz, z_roz
def set_axis_limits(ax, x_data, y_data, z_data, margin=0.1):
    x_min, x_max = np.min(x_data), np.max(x_data)
    y_min, y_max = np.min(y_data), np.max(y_data)
    z_min, z_max = np.min(z_data), np.max(z_data)

    if x_min == x_max:
        x_min -= margin
        x_max += margin
    if y_min == y_max:
        y_min -= margin
        y_max += margin
    if z_min == z_max:
        z_min -= margin
        z_max += margin

    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    ax.set_zlim([z_min, z_max])

# Przedział czasu
t = np.linspace(0, 1000, 100000)  # start, stop, gęstość punktów

# Rozwiązanie układu równań różniczkowych
t, x_roz, y_roz, z_roz = roz_uklad(x0, y0, z0, t)

# Tworzenie wykresu 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
set_axis_limits(ax, x_roz, y_roz, z_roz)
trace, = ax.plot([], [], [], lw=0.5)

def init():
    trace.set_data([], [])
    trace.set_3d_properties([])
    return trace,

def update(frame):
    trace.set_data(x_roz[:frame], y_roz[:frame])
    trace.set_3d_properties(z_roz[:frame])
    return trace,

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, interval=1)

plt.show()