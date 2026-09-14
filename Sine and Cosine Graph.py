import numpy as np
import matplotlib.pyplot as plt
Amplitude = 2
period = 24
num_periods = 2
x = np.linspace(0, period * num_periods, 1000)
y_sine = 2 * np.sin((np.pi / 12) * x)
y_cosine = 2 * np.cos((np.pi / 12) *x)
plt.plot(x, y_sine, label='2 * np.sin((np.sin / 12) * x)', color='green', linestyle='--')
plt.plot(x, y_cosine, label='2 * np.cos((np.cos / 12) *x)', color='red', linestyle='-.')
plt.title('Sine and Cosine Graph')
plt.xlabel('f(t)')
plt.ylabel('t')
plt.legend()
plt.grid(True)
plt.show()
