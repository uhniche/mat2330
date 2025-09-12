import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Example ODE: dy/dt = -2ty
def ode(t, y):
    return 2*y

# Time span and evaluation points
t_span = (0, 3)
t_eval = np.linspace(*t_span, 300)

# Initial conditions to plot
initial_conditions = [1, 0.5, -0.5, -1]

plt.figure(figsize=(8, 6))

for y0 in initial_conditions:
    sol = solve_ivp(ode, t_span, [y0], t_eval=t_eval)
    plt.plot(sol.t, sol.y[0], label=f"y(0) = {y0}")

# Elegant styling
plt.title("Solution Curves of dy/dt = 2y", fontsize=16)
plt.xlabel("t", fontsize=14)
plt.ylabel("y(t)", fontsize=14)
plt.grid(alpha=0.3)
plt.legend(frameon=True, fontsize=12)
plt.tight_layout()

# Save figure as PNG
plt.savefig("solution_curves.png", dpi=300)
plt.close()