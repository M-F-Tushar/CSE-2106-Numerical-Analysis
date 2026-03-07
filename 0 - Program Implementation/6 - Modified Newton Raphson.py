import math

# Function
def f(x):
    return 3*x - math.cos(x) - 1

# Derivative
def df(x):
    return 3 + math.sin(x)

def modified_newton_raphson(x0=0.5, iterations=5):
    fprime = df(x0)   # Compute derivative ONCE — never again!
    print(f"Fixed derivative f'(x0) = {fprime:.4f}\n")
    print(f"{'Iteration':<12} {'Root Approximation'}")

    x1 = x0
    for i in range(1, iterations + 1):
        x1 = x0 - f(x0) / fprime   # Always divide by the SAME fprime
        print(f"{i:<12} {x1:.6f}")
        x0 = x1

    print(f"\nApproximate root = {x1:.6f}")
    return x1

# Run the method
modified_newton_raphson(x0=0.5)
