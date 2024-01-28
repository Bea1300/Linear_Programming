from scipy.optimize import linprog

# Objective function coefficients (maximize profit)
c = [-5, -6, -7, -4, -3, -8, -7, -6, -2, -1, -2, -3, -2, -4,]  # Coefficients for P1, P2, P3, P4, P5 in A, B, C

# Coefficient matrix for inequalities (left-hand side of constraints)
A = [
    [-1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0],  # Labor hours constraint for A: -P1A - P2A - P3A - P4A - P5A <= -200
    [0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1],  # Labor hours constraint for B: -P1B - P2B - P3B - P4B - P5B <= -150
    [0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0],  # Labor hours constraint for C: -P1C - P2C - P3C - P4C - P5C <= -100
    [-1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Raw material constraint for A: -P1A - P2A - P3A - P4A - P5A <= -50
    [0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0],  # Raw material constraint for B: -P1B - P2B - P3B - P4B - P5B <= -100
    [0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0],  # Raw material constraint for C: -P1C - P2C - P3C - P4C - P5C <= -75
]

# Right-hand side of inequalities
b = [-200, -150, -100, -50, -100, -75]

# Bounds for variables
x_bounds = (0, None)  # Production quantities must be non-negative

# Solving the linear programming problem for maximization
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds] * 15, method='highs')

# Extracting optimal values
optimal_quantities = result.x

# Displaying the result
print("Optimal production quantities:")
for i in range(5):
    print(f"Product {i+1}:")
    for j in range(3):
        print(f"  Plant {chr(ord('A') + j)}: {optimal_quantities[i * 3 + j]}")
print("Optimal total profit:", -result.fun)  # Note the negation for maximization
