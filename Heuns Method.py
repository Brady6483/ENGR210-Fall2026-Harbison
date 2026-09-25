import numpy as np
def f(t, y):
    return -1000 * y + 3000 - 2000 * np.exp(-t)
def exact_sol(t):
    return 3 - 0.998 * np.exp(-1000 * t) - 2.002 * np.exp(-t)
def heuns_method(f, y0, t0, tf, h):
    steps = int((tf - t0) / h)
    t = np.linspace(t0, tf, steps + 1)
    y = np.zeros(steps + 1)
    y[0] = y0
    for i in range(steps):
        y_predict = y[i] + h * f(t[i], y[i])
        y[i+1] = y[i] + (h / 2) * (f(t[i], y[i]) + f(t[i+1], y_predict))
    return t, y
y0 = 0
t0 = 0
tf = 0.02
step_sizes = [0.001, 0.0005, 0.00025, 0.000125]
print(f"{'Step Size (h)':<15}{'Max Absolute Error':<25}")
prev_error = None
for h in step_sizes:
    t, y_numerical = heuns_method(f, y0, t0, tf, h)
    y_exact = exact_sol(t)
    max_error = np.max(np.abs(y_numerical - y_exact))
    if prev_error is not None:
        rate = np.log2(prev_error / max_error)
        print(f"{h:<15.6f}{max_error:<25.5e}")
    else:
        print(f"{h:<15.6f}{max_error:<25.5e}")
prev_error = max_error
