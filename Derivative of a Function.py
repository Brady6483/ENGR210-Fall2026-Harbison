import numpy as np
import matplotlib.pyplot as plt

def get_derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)
if __name__ == "__main__":
    x_values = np.linspace(0, 2 * np.pi, 200)
    num_slope = get_derivative(np.sin, x_values, h=0.1)
    true_slope = np.cos(x_values)
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, num_slope, label="Numerical Slope")
    plt.plot(x_values, true_slope, label="True Slope", linestyle="--")
    plt.title("Numerical vs True")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    stepsizes = [10.0**(-i) for i in range(7)]
    error_list = []
for h in stepsizes:
    calculated = get_derivative(np.sin, x=1.0, h=h)
    actual = np.cos(1.0)
    error = abs(calculated - actual)
    error_list.append(error)
plt.figure(figsize=(10, 5))
plt.plot(stepsizes, error_list)
plt.xscale("log")
plt.yscale("log")
plt.title("Error vs Step Size")
plt.xlabel("Step Size")
plt.ylabel("Absolute Error")
plt.grid(True)
plt.show()