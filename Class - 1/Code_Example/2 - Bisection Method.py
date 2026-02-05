import math

def f(x):
    return 3*x - math.cos(x) - 1

def bisection(a , b, tolerance, max_iterations):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have different signs. ")
        return 0
    
    print("Iteration\t a\t\t b\t\t c\t\t f(c)")
    
    for i in range(1 , max_iterations + 1):
        c = (a + b) / 2
        print(f"{i}\t\t {a}\t {b}\t {c}\t {f(c)}")
        
        
        if abs(f(c)) < tolerance:
            print(f"Root found within tolerance ")
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    print("Maximum iterations reached. ")
    return c

a = 0
b = 1
tolerance = 1e-6
max_iterations = 50

root = bisection(a, b, tolerance, max_iterations)
print(f"Approximate root: {root}")