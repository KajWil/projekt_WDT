import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

# Stałe (og, które badał Rossler)
a = 0.2
b = 0.2
c = 5.7

def uklad(u, t):
    x, y, z = u
    dxdt = - y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

def roz_uklad(x0, y0, z0, t):
    warunki = [x0, y0, z0]
    roz = odeint(uklad, warunki, t)
    x_roz = roz[:, 0]
    y_roz = roz[:, 1]
    z_roz = roz[:, 2]
    return t, x_roz, y_roz, z_roz

# Przykładowe wartości początkowe
x0 = 0
y0 = 0
z0 = 0

# Przedział czasu
t = np.linspace(0, 1000, 10000)  # start, stop, gęstość punktów

# Rozwiązanie układu równań różniczkowych
t, x_roz, y_roz, z_roz = roz_uklad(x0, y0, z0, t)

# Tworzenie wykresu 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([np.min(x_roz), np.max(x_roz)])
ax.set_ylim([np.min(y_roz), np.max(y_roz)])
ax.set_zlim([np.min(z_roz), np.max(z_roz)])
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