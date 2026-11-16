import math as m
def Bisection(f, bracket, abs_tol):
    xL, xU = bracket
    iters = m.ceil(m.log((xU - xL)/abs_tol)/m.log(2) - 1)
    fxL = f(xL)
    fxU = f(xU)
    for i in range(iters):
        xR = (xL + xU)/2
        fxR = f(xR)
        if fxR == 0:
            break
        elif fxR*fxL < 0:
            xU = xR
            fxU = fxR
        else:
            xL = xR
            fxL = fxR
        print(xL, xU)
    return (xL + xU)/2
if __name__=='__main__':
    def tank_func(h):
        R, V = 3 , 30
        return m.pi * h**2 * (3*R -h)/3 - V
    result = Bisection(tank_func, (0,6), 0.01)
    print(result, 'depth in m')