from scipy.optimize import fsolve
import math
# Define the logarithmic function f(x) = x * log(x) - 2048 * log(2)
def log_func(x):
    return x * math.log(x) - 2048 * math.log(2)

# Solve the equation numerically with an initial guess
x_initial_guess = 10
solution = fsolve(log_func, x_initial_guess)[0]
print(solution)
