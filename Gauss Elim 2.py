import numpy as np
A = np.array([
    [1.0, -1.0, 2.0, -1.0],
    [1.0, 1.0, 1.0, 0.0],
    [2.0, -2.0, 3.0, -3.0],
    [1.0, -1.0, 4.0, 3.0]
])
b = np.array([-8.0, -2.0, -20.0, 4.0])
n = len(b)
M = np.zeros((n, n + 1))
M[:, :n] = A
M[:, n] = b
for i in range(n):
    for j in range(i + 1, n):
        factor = M[j, i] / M[i, i]
        M[j] = M[j] - factor * M[i]
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    total = M[i, -1]
    for j in range(i + 1, n):
        total -= M[i, j] * x[j]
    x[i] = total / M[i, i]
print(f"x1 = {x[0]}")
print(f"x2 = {x[1]}")
print(f"x3 = {x[2]}")
print(f"x4 = {x[3]}")
