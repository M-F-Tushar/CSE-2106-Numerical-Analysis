import math

# g(x) = (cos(x) + 1) / 3  —  the iteration function
def g(x):
    return (math.cos(x) + 1) / 3

def fixed_point_iteration(x0=0, iterations=5):
    print(f"{'Iteration':<12} {'Root Approximation'}")

    x1 = x0
    for i in range(1, iterations + 1):
        x1 = g(x0)           # Apply the iteration
        print(f"{i:<12} {x1:.6f}")
        x0 = x1              # Update: new x becomes the input

    print(f"\nApproximate root = {x1:.6f}")
    return x1

# Run the method
fixed_point_iteration(x0=0)
