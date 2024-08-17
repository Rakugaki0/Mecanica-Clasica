import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros iniciales
r1 = 1
r2 = 4
theta = np.pi / 6
h2 = 2 * 9.8 * r1**2 * r2**2 * np.sin(theta)**2 * np.cos(theta) / (r1 + r2)
x0 = [r1, 0, 0]  # Condiciones iniciales [r, dr/dt, phi]

# Definir las ecuaciones diferenciales
def sistema(t, x):
    r, dr_dt, phi = x
    d2r_dt2 = h2 / (r**3 * np.sin(theta)**2) - 9.8 * np.cos(theta)
    dphi_dt = np.sqrt(h2) / (r**2 * np.sin(theta)**2)
    return [dr_dt, d2r_dt2, dphi_dt]

# Intervalo de tiempo
t_span = (0, 20)
t_eval = np.linspace(*t_span, 1000)

# Resolver el sistema
sol = solve_ivp(sistema, t_span, x0, t_eval=t_eval)

# Coordenadas cartesianas
xp = sol.y[0] * np.cos(sol.y[2]) * np.sin(theta)
yp = sol.y[0] * np.sin(sol.y[2]) * np.sin(theta)
zp = sol.y[0] * np.cos(theta)

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
