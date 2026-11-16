import math as m
def g(h):
    R, V = 3, 30
    return m.sqrt((3*V/m.pi + h**3) / (3*R))
def dg(h):
    R, V = 3, 30
    return (3*h**2) / (2 * m.sqrt((3*V/m.pi + h**3) * (3*R)))
if __name__=='__main__':
    print("g(2.0) =", g(2.0))
    print("|g'(2.0)| =", abs(dg(2.0)))