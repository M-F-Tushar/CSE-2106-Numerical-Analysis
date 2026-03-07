import math

# Function definition
def f(x):
    return 3*x - math.cos(x) - 1

def secant_method(x0=0, x1=1, iterations=5):
    print(f"{'Iteration':<12} {'Root Approximation'}")

    x2 = x1
    for i in range(1, iterations + 1):
        # Secant formula: approximate slope using two previous points
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"{i:<12} {x2:.6f}")

        # Slide the window forward
        x0 = x1
        x1 = x2

    print(f"\nApproximate root = {x2:.6f}")
    return x2

# Run the method
secant_method(x0=0, x1=1)
