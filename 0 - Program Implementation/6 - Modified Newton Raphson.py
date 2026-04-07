import math

def f(x):
    return 3*x - math.cos(x) - 1

def df(x):
    return 3 + math.sin(x)

def modified_newton_raphson(x0, iterations = 5):
    fprime = df(x0)
    print(f"Fixed derivative f'(x0) = {fprime:.4f}")
    print(f"{'Iteration:<12'} {'Root Approximation'}")
    
    x1 = x0
    for i in range(1, iterations + 1):
        x1 = x0 - f(x0) /fprime
        print(f"{i:<12} {x1:<12}")
        x0 = x1
        
    print(f"\nApproximate root = {x1:.6f}")
    return x1
modified_newton_raphson(0.5)
