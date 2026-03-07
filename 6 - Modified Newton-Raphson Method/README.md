# The Modified Newton-Raphson Method
## Same Power, Less Computation

---

## 🧠 The Problem with Standard Newton-Raphson

Standard Newton-Raphson is blazing fast, but it has a cost: **you must recompute the derivative at every single iteration.**

For simple functions like `f'(x) = 3 + sin(x)`, that's no big deal.

But imagine a more complex function where computing the derivative is:
- Mathematically complicated
- Computationally expensive
- Or involving measurements that can't be redone cheaply

In these cases, computing `f'(xₙ)` fresh every iteration is wasteful.

**The Modified Newton-Raphson Method says:** *"Compute the derivative ONCE at the starting point, and reuse it forever."*

---

## 🔄 What Changes?

In standard Newton-Raphson:
```
xₙ₊₁ = xₙ − f(xₙ) / f'(xₙ)   ← derivative updates every step
```

In Modified Newton-Raphson:
```
xₙ₊₁ = xₙ − f(xₙ) / f'(x₀)   ← derivative is FIXED from initial guess
```

Notice the denominator: it always uses `f'(x₀)` — the derivative at the **initial guess** — not the current point.

---

## 🏭 Story Example — The Assembly Line

Imagine a factory that calibrates machines. The standard method recalibrates every single time a product comes through — very accurate, but expensive.

The modified method says: *"Let's calibrate once at the start of the day, and use that calibration for the whole shift."*

It's slightly less precise per step, but **much cheaper to run.** And for well-behaved functions, it still converges to the exact same answer.

---

## 📖 Solving `f(x) = 3x − cos(x) − 1`

### Setup

```
f(x) = 3x − cos(x) − 1
f'(x) = 3 + sin(x)
```

Choose initial guess `x₀ = 0.5`

Compute the derivative **once and for all**:
```
f'(x₀) = f'(0.5) = 3 + sin(0.5)
                 = 3 + 0.4794
                 = 3.4794
```

This value `3.4794` will be used in **every single iteration**.

---

### Iteration Formula

```
xₙ₊₁ = xₙ − f(xₙ) / 3.4794
```

---

### Iteration 1

```
f(0.5) = 3(0.5) − cos(0.5) − 1
       = 1.5 − 0.8776 − 1
       = −0.3776

x₁ = 0.5 − (−0.3776) / 3.4794
   = 0.5 + 0.1085
   = 0.6085
```

Same as standard Newton-Raphson so far (because we start from the same point)!

---

### Iteration 2

```
f(0.6085) = 3(0.6085) − cos(0.6085) − 1
          = 1.8255 − 0.8202 − 1
          = 0.0053

x₂ = 0.6085 − 0.0053 / 3.4794    ← Still using 3.4794 from x₀!
   = 0.6085 − 0.00152
   = 0.6070
```

---

### Iteration 3

```
f(0.6070) ≈ 0   →   x₃ ≈ 0.607
```

**Converged!** ✅

---

### Side-by-Side Comparison

| Iteration | Standard N-R | Modified N-R |
|---|---|---|
| 1 | 0.608519 | 0.608519 |
| 2 | 0.607102 | 0.607064 |
| 3 | 0.607102 | 0.607103 |
| 4 | 0.607102 | 0.607102 |

They reach the **same answer** — Modified N-R just takes one extra tiny step because the fixed denominator is slightly "wrong" for later iterations. But the difference is negligible.

---

## 🐍 Python Code

```python
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
```

### Output

```
Fixed derivative f'(x0) = 3.4794

Iteration    Root Approximation
1            0.608519
2            0.607064
3            0.607103
4            0.607102
5            0.607102

Approximate root = 0.607102
```

---

## ⚖️ Standard vs Modified Newton-Raphson

| Feature | Standard N-R | Modified N-R |
|---|---|---|
| Derivative computation | Every iteration | Once at start |
| Convergence speed | Quadratic (very fast) | Linear (slightly slower) |
| Computation cost | Higher | Lower |
| Same final answer? | Yes | Yes (usually) |
| Best for | Any function | Expensive derivatives |

---

## 🎯 Key Takeaways

- Modified Newton-Raphson computes `f'(x)` **only once** at the initial guess.
- It reuses that fixed derivative value in every iteration.
- Slightly slower convergence than standard Newton-Raphson, but much cheaper computationally.
- In practice, when `f'(x)` is expensive to compute, the Modified method is preferred.
- Real root for `f(x) = 3x − cos(x) − 1`: **x ≈ 0.607102**
