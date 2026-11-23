import math as m
def golden_section_opt(f, xl, xu, tol = 1e-6):
    R = (m.sqrt(5) -1) / 2.0
    d = R * (xu - xl)
    x1 = xl + d
    x2 = xu - d
    f1 = f(x1)
    f2 = f(x2)
    while abs(xu - xl) > tol:
        if f1 > f2:
            xl = x2
            x2 = x1
            f2 = f1
            d = R * (xu - xl)
            x1 = xl + d
            f1 = f(x1)
        else:
            xu = x1
            xl = x2
            f1 = f2
            d = R * (xu - xl)
            x2 = xu - d
            f2 = f(x2)
    return (xl + xu) / 2.0
#3
def parabola(x):
    a, b, c = -2, 8, 5
    return a * x**2 + b * x + c
x_parabola = golden_section_opt(parabola, -5, 5)
print("Optimum Parabola x =", round(x_parabola, 5))
x_sin = golden_section_opt(m.sin, 0, m.pi)
print("Optimum Sine x =", round(x_sin, 5))
#4
def profit(A0):
    K = 2
    B0 = 100
    low = 0.0
    high = min(A0 / 2, B0)
    for i in range(60):
        C = (low + high) / 2
        if K * (A0 - 2 * C) ** 2 * (B0 - C) - C > 0:
            low = C
        else:
            high = C
    return 10 * C - A0
best_A0 = golden_section_opt(profit, 0, 400, tol=1e-5)
print("Optimum A0 =", round(best_A0, 3))
print("Max Profit =", round(profit(best_A0), 2))
#5
def deflection(x):
    L = 400
    E = 52000
    I = 32000
    w = 4
    return (w / (48 * E * I)) * (2 * x**4 - 3 * L * x**3 + L**3 * x)
best_x = golden_section_opt(deflection, 0, 400)
print("Max Deflection of x =", round(best_x, 2))
print("Max Deflection of y =", round(deflection(best_x), 4))