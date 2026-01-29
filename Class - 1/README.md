# Numerical Analysis Lab Course

## 1. How Absolute Error Is Calculated

### Definition
Absolute Error measures how far an approximate value is from the true value.

### Formula
```
Absolute Error = |True Value - Approximate Value|
```

### Example
If:
- True value = 3.0
- Approximate value = 2.0

Then:
```
Absolute Error = |3.0 - 2.0| = 1.0
```

## 2. How Relative Error Is Calculated

### Definition
Relative Error shows the absolute error relative to the true value.
It tells how large the error is in proportion to the true value.

### Formula
```
Relative Error = |True Value - Approximate Value| / |True Value|
```

### Example
Using the same values:
```
Relative Error = 1.0 / 3.0 = 0.3333
```

## Percentage Error

### Definition
Percentage Error expresses the error as a percentage of the true value.
It is obtained by multiplying the relative error by 100.

### Formula
```
Percentage Error = (|True Value - Approximate Value| / |True Value|) × 100%
```

### Example
If:
- True value = 3.0
- Approximate value = 2.0

Then:

1. **Absolute Error**
   ```
   |3.0 - 2.0| = 1.0
   ```

2. **Relative Error**
   ```
   1.0 / 3.0 = 0.3333
   ```

3. **Percentage Error**
   ```
   0.3333 × 100 = 33.33%
   ```

### Code:
```python
# Input true and approximate values
true_value = float(input("Enter true value: "))
approx_value = float(input("Enter approximate value: "))

# Absolute Error
absolute_error = abs(true_value - approx_value)

# Relative Error
relative_error = absolute_error / abs(true_value)

# Percentage Error
percentage_error = relative_error * 100

print(f"\nAbsolute Error = {absolute_error}")
print(f"Relative Error = {relative_error}")
print(f"Percentage Error = {percentage_error}%")
```

## Bisection Method

### Definition
The root of a function is a value of the variable for which the function becomes zero.

f(x) = 0, then the value x is called a root (or zero) of the function.

### Example 1
Let:
```
f(x) = x² - 4
```

Solve:
```
x² - 4 = 0
```
- Roots are x = -2 and x = 2

## Solve the root of f(x) = 3x - cos(x) - 1
using the Bisection Method step by step, including the procedure, iterations, and Python code.

### Step 1: Define the function
```
f(x) = 3x - cos(x) - 1
```
We want to find x such that f(x) = 0.

### Step 2: Find an interval [a, b] where a root exists
We need f(a) · f(b) < 0.

Let's try some values:

1. x = 0 → f(0) = 3(0) - cos(0) - 1 = -1 - 1 = -2
2. x = 1 → f(1) = 3(1) - cos(1) - 1 ≈ 3 - 0.5403 - 1 ≈ 1.4597

Sign changes between 0 and 1 — root exists in [0, 1]

### Step 3: Bisection Method Procedure

1. Compute midpoint:
   ```
   c = (a + b) / 2
   ```

2. Evaluate f(c)
   - If f(c) = 0 — root found
   - Else:
     - If f(a) · f(c) < 0 — root is in [a, c] → set b = c
     - Else — root is in [c, b] → set a = c

3. Repeat until |f(c)| < tolerance or max iterations reached.

### Step 5: Sample Iterations (First few)

| Iteration | a       | b       | c       | f(c)     |
|-----------|---------|---------|---------|----------|
| 1         | 0       | 1       | 0.5     | -0.0203  |
| 2         | 0.5     | 1       | 0.75    | 0.4746   |
| 3         | 0.5     | 0.75    | 0.625   | 0.2220   |
| 4         | 0.5     | 0.625   | 0.5625  | 0.1006   |
| 5         | 0.5     | 0.5625  | 0.53125 | 0.0399   |
| 6         | 0.5     | 0.53125 | 0.51563 | 0.0098   |
| 7         | 0.5     | 0.51563 | 0.50781 | -0.0052  |
| 8         | 0.50781 | 0.51563 | 0.51172 | 0.0023   |

...and so on until |f(c)| < 1e-6

### Code:
```python
import math

# Define the function f(x) = 3x - cos(x) - 1
def f(x):
    return 3*x - math.cos(x) - 1

# Bisection Method
def bisection(a, b, tolerance, max_iterations):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return 0
    
    print("Iteration\t a\t\t b\t\t c\t\t f(c)")
    
    for i in range(1, max_iterations + 1):
        c = (a + b) / 2
        print(f"{i}\t\t {a}\t {b}\t {c}\t {f(c)}")
        
        # Check stopping condition
        if abs(f(c)) < tolerance:
            print("\nRoot found within tolerance.")
            return c
        
        # Update interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    print("\nMaximum iterations reached.")
    return c

# Main
a = 0
b = 1
tolerance = 1e-6
max_iterations = 50

root = bisection(a, b, tolerance, max_iterations)
print(f"\nApproximate Root = {root}")
```

