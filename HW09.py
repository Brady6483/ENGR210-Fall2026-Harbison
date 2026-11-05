import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Parameters
# --------------------------

k = 25.0

ho = 1000.0
To = 1700.0

hi = 200.0
Ti = 400.0

W = 10e-3
H = 6e-3

Nx = 51
Ny = 31

dx = W/(Nx-1)
dy = H/(Ny-1)

T = np.ones((Ny,Nx))*1000

# --------------------------
# Channel geometry
# --------------------------

x = np.linspace(0,W,Nx)
y = np.linspace(0,H,Ny)

channel = np.zeros((Ny,Nx),dtype=bool)

x1 = 2e-3
x2 = 8e-3

y1 = 2e-3
y2 = 4e-3

for j in range(Ny):
    for i in range(Nx):
        if x1 <= x[i] <= x2 and y1 <= y[j] <= y2:
            channel[j,i] = True

# --------------------------
# Gauss-Seidel
# --------------------------

tol = 1e-6
error = 1

while error > tol:

    old = T.copy()

    for j in range(1,Ny-1):
        for i in range(1,Nx-1):

            if channel[j,i]:
                continue

            T[j,i] = 0.25*(
                T[j+1,i]+
                T[j-1,i]+
                T[j,i+1]+
                T[j,i-1]
            )

    Bi_o = ho*dy/k

    for i in range(Nx):

        T[Ny-1,i] = (
            T[Ny-2,i]
            + Bi_o*To
        )/(1+Bi_o)

        T[0,i] = (
            T[1,i]
            + Bi_o*To
        )/(1+Bi_o)

    T[:,0] = T[:,1]
    T[:,-1] = T[:,-2]

    error = np.max(np.abs(T-old))

print("Converged")

Tmax = np.max(T)
loc = np.unravel_index(np.argmax(T),T.shape)

print("Maximum Temperature =",Tmax)
print("Location =",loc)

plt.contourf(x*1000,y*1000,T,30)
plt.colorbar(label='Temperature (K)')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.show()