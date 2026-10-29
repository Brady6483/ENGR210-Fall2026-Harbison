import numpy as np
import matplotlib.pyplot as plt
L = 10.0
h_prime = 0.01
Ta = 20.0
T0 = 200.0
Tb = 40.0
def analytical_solution(x):
    num = np.cosh(np.sqrt(h_prime) * (L -x))
    den = np.cosh(np.sqrt(h_prime) * L)
    return Ta + (T0 - Ta) * (num / den)
def solve_fdm(dx):
    N = int(L / dx)
    x = np.linspace(0, L, N + 1)
    A = np.zeros((N + 1, N + 1))
    B = np.zeros(N + 1)
    A[0, 0] = 1
    B[0] = T0
    A[N, N-1] = 2
    A[N, N] = -(2 + h_prime * dx**2)
    B[N] = -h_prime * dx**2 * Ta
    for i in range(1, N):
        A[i, i-1] = 1
        A[i, i] = -(2 + h_prime * dx**2)
        A[i, i+1] = 1
        B[i] = -h_prime * dx**2 * Ta
    T = np.linalg.solve(A, B)
    return x, T
step_sizes = [1.0, 0.1, 0.01]
plt.figure(figsize=(10, 6))
x_exact = np.linspace(0, L, 1000)
T_exact = analytical_solution(x_exact)
plt.plot(x_exact, T_exact, 'k--', label='Analytical Solution', linewidth=2)
for dx in step_sizes:
    x_fdm, T_fdm = solve_fdm(dx)
    plt.plot(x_fdm, T_fdm, label='Finite Difference')
plt.title('Temperature Profile along a 10m rod')
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (C)')
plt.show()
dx_values = [1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
errors = []
for dx in dx_values:
    x_fdm, T_fdm = solve_fdm(dx)
    T_exact_nodes = analytical_solution(x_fdm)
    rmse = np.sqrt(np.mean((T_fdm - T_exact_nodes)**2))
    errors = np.append(errors, rmse)
plt.figure(figsize=(6, 5))
plt.loglog(dx_values, errors, 'o-', label='Finite Difference Error')
plt.loglog(dx_values, [errors[-1] * (dx / dx_values[-1])**2 for dx in dx_values], 'k--', label='Slope')
plt.title('Convergence Analysis')
plt.xlabel('Step Size (m)')
plt.ylabel('Error Norm')
plt.legend()
plt.show()
