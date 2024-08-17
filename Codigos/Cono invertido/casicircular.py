import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros iniciales
r0 = 2.25
theta = np.pi / 3
w = np.sqrt(9.8 * np.cos(theta) / r0) / np.sin(theta)
W = np.sqrt(3 * 9.8 * np.cos(theta) / r0)
t = np.linspace(0, 2 * np.pi * W / w, 1000)

# Cálculo de r y phi
r = r0 + 0.25 * np.sin(W * t)
phi = w * t - 2 * (0.25 / r0) * (w / W) * np.sin(W * t)

# Coordenadas cartesianas
xp = r * np.cos(phi) * np.sin(theta)
yp = r * np.sin(phi) * np.sin(theta)
zp = r * np.cos(theta)

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Superficie cónica
phi_surf = np.linspace(0, 2 * np.pi, 40)
r_surf = np.linspace(0, 4)
phi_surf, r_surf = np.meshgrid(phi_surf, r_surf)
x_surf = r_surf * np.cos(phi_surf) * np.sin(theta)
y_surf = r_surf * np.sin(phi_surf) * np.sin(theta)
z_surf = r_surf * np.cos(theta)
ax.plot_surface(x_surf, y_surf, z_surf, color='gray', alpha=0.5, edgecolor='none')

# Trayectoria
ax.plot(xp, yp, zp, color='red', linewidth=1.5)

# Configuración de la vista y etiquetas
ax.view_init(elev=70, azim=120)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Movimiento en una superficie cónica')

plt.show()
