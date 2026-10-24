import numpy as np

A2 = np.array([
    [1.0, -1.0, 2.0, -1.0],
    [1.0, 1.0, 1.0, 0.0],
    [2.0, -2.0, 3.0, -3.0],
    [1.0, -1.0, 4.0, 3.0]
])
b2 = np.array([-8.0, -2.0, -20.0, 4.0])
sol4 = np.linalg.solve(A2, b2)
print(f"x1 = {sol4[0]}")
print(f"x2 = {sol4[1]}")
print(f"x3 = {sol4[2]}")
print(f"x4 = {sol4[3]}")
