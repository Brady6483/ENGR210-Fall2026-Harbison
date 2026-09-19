import matplotlib.pyplot as plt
import numpy as np
def integrals(f, x0, xN, N):
    h = (xN - x0) / N
    x = np.linspace(x0, xN, N + 1)
    y = f(x)
    integral = h * ( (y[0] + y[-1]) / 2 + np.sum(y[1:-1]) )
    return integral
def f(x):
    return x**2
def true_integral(x0, xN):
    return (xN**3 / 3) - (x0**3 / 3)
x0 = 0
N_fixed = 100
xN_values = np.linspace(1, 10, 50)
integral_values = [integrals(f, x0, xN, N_fixed) for xN in xN_values]
xN_fixed = 1
N_values = np.array([10, 20, 50, 100, 200, 500, 1000])
h_values = (xN_fixed - x0) / N_values
exact_val = true_integral(x0, xN_fixed)
errors = [abs(exact_val - integrals(f, x0, xN_fixed, N)) for N in N_values]
errors = np.array(errors)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(xN_values, integral_values, 'b-', label='Approximate Integral')
plt.xlabel('Variable x_N')
plt.ylabel('Integral Value')
plt.title('Integral Value vs. x_N')
plt.grid(True)
plt.legend()
plt.subplot(1, 2, 2,)
plt.loglog(h_values, errors, 'ro-', label='Measured Error')
plt.loglog(h_values, h_values**2 * (errors[0]/h_values[0]**2), 'k--', label='O(h^2) Reference')
plt.xlabel('Step Size h')
plt.ylabel('Absolute Error')
plt.title('Error vs. h')
plt.grid(True,)
plt.legend()
plt.show()
