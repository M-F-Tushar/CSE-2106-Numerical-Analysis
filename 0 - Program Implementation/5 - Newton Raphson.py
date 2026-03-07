import math

# The function f(x)
def f(x):
    return 3*x - math.cos(x) - 1

# The derivative f'(x)
def df(x):
    return 3 + math.sin(x)

def newton_raphson(x0=0.5, iterations=5):
    print(f"{'Iteration':<12} {'Root Approximation'}")

    x1 = x0
    for i in range(1, iterations + 1):
        # Newton-Raphson formula
        x1 = x0 - f(x0) / df(x0)
        print(f"{i:<12} {x1:.6f}")
        x0 = x1

    print(f"\nApproximate root = {x1:.6f}")
    return x1

# Run the method
newton_raphson(x0=0.5)
