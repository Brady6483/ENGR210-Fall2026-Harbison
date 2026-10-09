import numpy as np
import matplotlib.pyplot as plt
k_growth = 0.3
k_predation = 0.01
k_death = 0.2
k_reprod = 0.0003
dt = 1 / 12
t_end = 40
steps = int(t_end / dt)
t = np.linspace(0, t_end, steps + 1)
def derivatives(x, y):
    d_prey = k_growth * x - k_predation * x * y
    d_pred = -k_death * y + k_reprod * x * y
    return  d_pred, d_prey
x_euler = np.zeros(steps + 1)
y_euler = np.zeros(steps + 1)
x_heun = np.zeros(steps + 1)
y_heun = np.zeros(steps + 1)
x_euler[0], y_euler[0] = 700, 22
x_heun[0], y_heun[0] = 700, 22
for n in range(steps):
    dx_e, dy_e = derivatives(x_euler[n], y_euler[n])
    x_euler[n+1] = x_euler[n] + dt * dx_e
    y_euler[n+1] = y_euler[n] + dt * dy_e
    dx_h1, dy_h1 = derivatives(x_heun[n], y_heun[n])
    x_pred = x_heun[n] + dt * dx_h1
    y_pred = y_heun[n] + dt * dy_h1
    dx_h2, dy_h2 = derivatives(x_pred, y_pred)
    x_heun[n+1] = x_heun[n] + (dt / 2) * (dx_h1 + dx_h2)
    y_heun[n+1] = x_heun[n] + (dt / 2) * (dy_h1 + dy_h2)
plt.subplot(3, 1, 1)
plt.plot(t, x_euler, 'r--', label='Euler Method', alpha = 0.8)
plt.plot(t, x_heun, 'b-', label='Heuns Method')
plt.title('Time Series Plot of Prey')
plt.xlabel('Time(Years)')
plt.ylabel('Prey Population')
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(t, y_euler, 'r--', label='Euler Method', alpha = 0.8)
plt.plot(t, y_heun, 'g-', label='Heuns Method')
plt.title('Time Series Plot of Predators')
plt.xlabel('Time(Years)')
plt.ylabel('Predator Population')
plt.legend()
plt.subplot(3, 1, 3,)
plt.plot(x_euler, y_euler, 'r--', label='Euler Method', alpha = 0.7)
plt.plot(x_heun, y_heun, 'm-', label='Heuns Method')
plt.scatter(700, 22, color='black', zorder=5, label="Initial Condition")
plt.title('State-Space Orbit (Predator vs. Prey)')
plt.xlabel('Prey Population')
plt.ylabel('Predator Population')
plt.legend()
plt.tight_layout()
plt.show()
    
