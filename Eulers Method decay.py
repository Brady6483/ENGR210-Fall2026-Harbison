import numpy as np
import matplotlib.pyplot as plt
def f(t, y):
    return -y
def euler_method(f, y0, t0, tf, dt):
    N = int((tf - t0)/dt) + 1
    t = np.linspace(t0, tf, N)
    y = np.zeros(N)
    y[0] = y0
    for i in range(0, N-1):
        y[i+1] = y[i] + dt * f(t[i], y[i])
    return t, y
def analytical_solution(t):
    return np.exp(-t)
def rmse(y_approx, y_true, dt):
    return np.sqrt(dt * np.sum((y_approx - y_true)**2))
y0 = 1.0
t0 = 0.0
tf = 5.0
steps = [0.1, 0.2, 0.5, 1.0, 1.5]
rmse_values = []
plt.figure(figsize=(10, 6))
for dt in steps:
    t, y_approx = euler_method(f, y0, t0, tf, dt)
    y_true = analytical_solution(t)
    error = rmse(y_approx, y_true, dt)
    rmse_values.append(error)
    plt.plot(t, y_approx, marker='o', label=f'Euler dt={dt}')
plt.plot(np.linspace(t0, tf, 100), analytical_solution(np.linspace(t0, tf, 100)), 'k--', label='Analytical')
plt.xlabel('Time t')
plt.ylabel('Solution y(t)')
plt.title("Euler Method vs Analytical Solution")
plt.legend()
plt.show()

