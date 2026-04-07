import math

def f(x):
    return 3*x - math.cos(x) -1

def regula_falsi(a, b, iterations = 5):
    if f(a) * f(b) >= 0:
        print("f(a) and f(b) must have opposite signs.")
        return None
    
    print(f"{'Iteration':<12} {'Root Approximation'}")
    
    x = None
    for i in range(1, iterations + 1):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"{i:<12} {x:.6f}")
        
        if f(x) == 0:
            break
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
        
    print(f"\nApproximate root = {x:.6f}")
    return x

regula_falsi(0, 1)
        
