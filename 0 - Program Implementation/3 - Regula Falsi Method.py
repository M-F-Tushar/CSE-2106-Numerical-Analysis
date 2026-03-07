import math

# Function definition
def f(x):
    return 3*x - math.cos(x) - 1

def regula_falsi(a, b, iterations=5):
    # Check that signs are opposite
    if f(a) * f(b) >= 0:
        print("Invalid initial guesses! f(a) and f(b) must have opposite signs.")
        return None

    print(f"{'Iteration':<12} {'Root Approximation'}")

    c = None
    for i in range(1, iterations + 1):
        # Regula Falsi formula — line crossing zero
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"{i:<12} {c:.6f}")

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c   # root in left portion
        else:
            a = c   # root in right portion

    print(f"\nApproximate root = {c:.6f}")
    return c

# Run the method
regula_falsi(a=0, b=1)
