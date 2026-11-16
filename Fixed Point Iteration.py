import math as m
def FixedPoint(g, x0, abs_tol):
    x_old = x0
    while True:
        x_new = g(x_old)
        print(x_new)
        if abs(x_new - x_old) < abs_tol:
            break
        x_old = x_new
    return x_new
if __name__=='__main__':
    def g_func(h):
        R, V = 3, 30
        return m.sqrt(3*V/m.pi + h**3) / (3*R)
    result = FixedPoint(g_func, 2.0, 0.01)
    print(result, 'depth in m')