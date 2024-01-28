import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Objective function coefficients (maximise)
c = [-4, -5]

# Coefficient matrix for inequalities (left-hand side of constraints)
A = [
    [2, 1],    # Constraint 1: 2x + y <= 20
    [-4, 5]    # Constraint 2: 4x - 5y >= -10
]

# Right-hand side of inequalities
b = [20, -10]

# Bounds for variables
x_bounds = (0, None)  # x >= 0
y_bounds = (0, None)  # y >= 0

# Solving the linear programming problem for maximization
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extracting optimal values
optimal_x = result.x[0]
optimal_y = result.x[1]

# Displaying the result
print("Optimal values:")
print("x =", optimal_x)
print("y =", optimal_y)
print("Optimal objective value:", -result.fun) 

# Generate points for plotting the constraints
x_values = np.linspace(0, 10, 100)
y_constraint1 = 20 - 2 * x_values  # Constraint 1: 2x + y <= 20
y_constraint2 = (4 * x_values + 10) / 5  # Constraint 2: 4x - 5y >= -10

# Plotting the constraints
plt.plot(x_values, y_constraint1, label='2x + y <= 20')
plt.plot(x_values, y_constraint2, label='4x - 5y >= -10')

# Plotting the feasible region
plt.fill_between(x_values, 0, np.minimum(y_constraint1, y_constraint2), where=(y_constraint1 >= 0) & (y_constraint2 >= 0), interpolate=True, alpha=0.3, color='gray', label='Feasible Region')

# Plotting the optimal solution
plt.scatter(optimal_x, optimal_y, color='red', marker='*', label='Optimal Solution')

# Adding labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Maximization Example')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Show the plot
plt.show()


