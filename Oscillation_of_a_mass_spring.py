import numpy as np
import matplotlib.pyplot as plt
m = 2
k = 20
x0 = 0.5
v0 = 0
dt = 0.1
T = 200
t = np.arange(0, T + dt, dt)
N = len(t)
omega = np.sqrt(k / m)
x_exact = x0 * np.cos(omega * t)
x_euler = np.zeros(N)
v_euler = np.zeros(N)
x_euler[0], v_euler[0] = x0, v0
for n in range(N - 1):
    x_euler[n+1] = x_euler[n] + v_euler[n] * dt
    v_euler[n+1] = v_euler[n] - (k / m) * x_euler[n] * dt
x_rk = np.zeros(N)
v_rk = np.zeros(N)
x_rk[0],  v_rk[0] = x0, v0
def  f(x, v):
    return np.array([v, -(k / m) * x])
for n in range(N - 1):
    state = np.array([x_rk[n], v_rk[n]])
    k1 = f(state[0], state[1])
    k2 = f(state[0] + 0.5 * dt * k1[0], state[1] + 0.5 * dt * k1[1])
    k3 = f(state[0] + 0.5 * dt * k2[0], state[1] + 0.5 * dt * k2[1])
    k4 = f(state[0] + dt * k3[0], state[1] + dt * k3[1])
    next_state = state + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)
    x_rk[n+1], v_rk[n+1] = next_state[0], next_state[1]
x_lf = np.zeros(N)
v_lf = np.zeros(N)
x_lf[0], v_lf[0] = x0, v0
for n in range(N - 1):
    v_half = v_lf[n] + 0.5 * (-(k / m) * x_lf[n]) * dt
    x_lf[n+1] = x_lf[n] + v_half * dt
    v_lf[n+1] = v_half + 0.5 * (-(k / m) * x_lf[n+1]) * dt
error_euler = np.abs(x_euler - x_exact)
error_rk = np.abs(x_rk - x_exact)
error_lf = np.abs(x_lf - x_exact)
plt.figure(figsize=(12, 6))
plt.plot(t, error_euler, label='Euler Error', color='red', alpha=0.7)
plt.plot(t, error_lf, label='LeapFrog Error', color='green', alpha=0.8)
plt.plot(t, error_rk, label='RK4 Error', color='blue', alpha=0.9)
plt.title('Displacement Absolute Error vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Absolute Error (meters)')
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.show()