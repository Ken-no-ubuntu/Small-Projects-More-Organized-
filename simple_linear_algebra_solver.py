import numpy as np
import sympy as sp


x, y, z = sp.symbols('x y z')


equation = sp.Eq(2*x + 3*y - z, 8)


lhs = equation.lhs - equation.rhs


coeff_x = lhs.coeff(x)
coeff_y = lhs.coeff(y)
coeff_z = lhs.coeff(z)


coefficients = [coeff_x, coeff_y, coeff_z]
num_coefficients = [float(coeff) for coeff in coefficients]
A = np.array([
    num_coefficients,
    [1,1,1],
    [2,3,4]
])

B=([[4],
    [5],
    [1]
    ])
C=np.linalg.solve(A, B)
print(f"The Grand Solution is:\n{C}".replace("["," ").replace("]"," "))