import numpy as np
m = 0.014
Cd = 1.3e-3
g = 9.81
def derivatives(state):
    x, y, vx, vy = state
    v = np.sqrt(vx**2 + vy**2)
    ax = -Cd * v * vx / m
    ay = -g - Cd * v * vy / m
    return np.array([vx, vy, ax, ay])
def rk4_step(state, dt):
    k1 = derivatives(state)
    k2 = derivatives(state + 0.5 * dt * k1)
    k3 = derivatives(state + 0.5 * dt * k2)
    k4 = derivatives(state + dt * k3)
    return state + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
def simulate(angle_deg, dt=0.001):
    angle = np.radians(angle_deg)
    vx0 = 22 * np.cos(angle)
    vy0 = 22 * np.sin(angle)
    state = np.array([0.0, 0.0, vx0, vy0])
    while True:
        prev_state = state.copy()
        state = rk4_step(state, dt)
        if state[1] <= 0 and prev_state[1] > 0:
            return state[0] 
def find_max_range():
    angles = np.arange(5, 86, 1)
    ranges = [simulate(a) for a in angles]
    max_idx = np.argmax(ranges)
    return angles[max_idx], ranges[max_idx]
if __name__ == "__main__":
    angle, dist = find_max_range()
    print("Best angle:", angle)
    print("Max range (m):", dist)