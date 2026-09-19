import numpy as np
filename = 'ENGR210 Fa2026 HW04 Prob2 Data(in).csv'
data = np.loadtxt(filename, delimiter=',', skiprows=1)
strain = data[:, 0]
stress = data[:, 1]
toughness = 0
i = 0
while i < len(strain) - 1:
    dx = strain[i+1] - strain[i]
    avg_y = (stress[i] + stress[i+1]) / 2
    toughness += avg_y *dx
    i = i + 1
print("Estimated Toughness:", toughness)