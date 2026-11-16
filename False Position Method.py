import math as m
def FalsePosition(f, bracket, abs_tol):
    xL, xU = bracket
    fxL = f(xL)
    fxU = f(xU)
    xR_old = xL
    while True:
        xR = xU - (fxU * (xL - xU)) / (fxL - fxU)
        fxR = f(xR)
        if fxR == 0 or abs(xR - xR_old) < abs_tol:
            break 
        elif fxR*fxL < 0:
            xU = xR
            fxU = fxR
        else:
            xL = xR
            fxL = fxR
        xR_old = xR
        print(xL, xU)
    return xR
if __name__=='__main__':
    def tank_func(h):
        R, V = 3 , 30
        return m.pi * h**2 * (3*R -h)/3 - V
#    print(my_func(32), my_func(64))
    result = FalsePosition(tank_func, (0,6), 0.01)
    print(result, 'depth in m')
