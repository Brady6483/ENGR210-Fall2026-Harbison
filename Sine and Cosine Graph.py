import numpy as np
import matplotlib.pyplot as plt
Amplitude = 2
period = 24
num_periods = 2
x = np.linspace(0, period * num_periods, 100)
y_sine = 2 * np.sin((np.pi / 12) * x)
y_cosine = 2 * np.cos((np.pi / 12) *x)

