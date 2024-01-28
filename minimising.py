import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Objective function coefficients (minimise)
c = [2, 3]

# Coefficient matrix for inequalities (left-hand side of constraints)
A = [
    [-1, 1],  # Constraint 1: -x + y <= 4
    [1, 2]    # Constraint 2: x + 2y <= 14
]

# Right-hand side of inequalities
b = [4, 14]

# Bounds for variables
x_bounds = (0, None)  # x >= 0
y_bounds = (0, None)  # y >= 0

# Solving the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extracting optimal values
optimal_x = result.x[0]
optimal_y = result.x[1]

# Generate points for plotting the constraints
x_values = np.linspace(0, 8, 100)
y_constraint1 = 4 + x_values  # Constraint 1: -x + y <= 4
y_constraint2 = (14 - x_values) / 2  # Constraint 2: x + 2y <= 14

# Plotting the constraints
plt.plot(x_values, y_constraint1, label='-x + y <= 4')
plt.plot(x_values, y_constraint2, label='x + 2y <= 14')

# Plotting the feasible region
plt.fill_between(x_values, np.minimum(y_constraint1, y_constraint2), where=(y_constraint1 >= 0) & (y_constraint2 >= 0), interpolate=True, alpha=0.3, color='gray', label='Feasible Region')

# Plotting the optimal solution
plt.scatter(optimal_x, optimal_y, color='red', marker='*', label='Optimal Solution')

# Adding labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Programming Example')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Show the plot
plt.show()

