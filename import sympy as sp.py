import sympy as sp

# Define the variables
x, y, z = sp.symbols('x y z')

# Define the equation
equation = sp.Eq(3*x - y, z)

# Solve the equation for x
solution = sp.solve(equation, x)
print(solution)
A= sp.expand("(2 + 3 * x + 4 * x * y)^60")
print(A)

