def rk4_step(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h*k1/2)
    k3 = f(t + h/2, y + h*k2/2)
    k4 = f(t + h,   y + h*k3)
    return y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

def solve_rk4(f, t0, y0, t_end, h):
    t = t0
    y = y0
    while t < t_end:
        y = rk4_step(f, t, y, h)
        t += h
    return y
def f(t, y):
    return -2*y
y_final = solve_rk4(f, 0.0, 1.0, 1.0, 0.1)
print("y(1.0) ≈", y_final)
