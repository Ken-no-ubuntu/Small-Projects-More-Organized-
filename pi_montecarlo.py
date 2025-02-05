import random
import math

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = 4 * (inside_circle / num_samples)
    return pi_estimate

# Example usage:
num_samples = 10000000  # Number of random points to generate
pi_estimate = estimate_pi(num_samples)
print(f"Estimated value of Pi with {num_samples} samples: {pi_estimate}")
