import math as m
def Newton(f, df, x0, abs_tol):
    x_old = x0
    while True:
        x_new = x_old - f(x_old) / df(x_old)
        print(x_new)
        if abs(x_new - x_old) < abs_tol:
            break
        x_old = x_new
    return x_new
if __name__=='__main__':
    def tank_func(h):
        R, V = 3, 30
        return (m.pi * h**2 * (3*R - h))/ 3 - V
    def df_func(h):
        R = 3
        return m.pi * h * (2*R - h)
    result = Newton(tank_func, df_func, 2.0, 0.01)
    print(result, 'depth in m')