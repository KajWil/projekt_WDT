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

#punkty stałe
s1x = (c + np.sqrt(c**2 - 4*a*b))/2
s1y = (-c - np.sqrt(c**2 - 4*a*b))/(2*a)
s1z = (c + np.sqrt(c**2 - 4*a*b))/(2*a)
s2x = (c - np.sqrt(c**2 - 4*a*b))/2
s2y = (-c + np.sqrt(c**2 - 4*a*b))/(2*a)
s2z = (c - np.sqrt(c**2 - 4*a*b))/(2*a)

print("Współrzędne pierwszego punktu stałego: ", s1x, s1y, s1z)
print("Współrzędne drugiego punktu stałego: ",s2x, s2y, s2z)

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
fixed_points, = ax.plot([s1x, s2x], [s1y, s2y], [s1z, s2z], 'ro')  # Dodanie punktów stałych

def init():
    trace.set_data([], [])
    trace.set_3d_properties([])
    return trace, fixed_points

def update(frame):
    trace.set_data(x_roz[:frame], y_roz[:frame])
    trace.set_3d_properties(z_roz[:frame])
    return trace, fixed_points

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, interval=1)

plt.show()