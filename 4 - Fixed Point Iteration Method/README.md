# The Fixed Point Iteration Method
## Finding Roots by Feeding a Function Back Into Itself

---

## 🧠 A Completely Different Strategy

All the methods we've seen so far (Bisection, Regula Falsi) work by **trapping a root inside an interval** and shrinking it. Fixed Point Iteration takes a completely different approach.

The idea is beautifully simple:

> **Rewrite the equation so it looks like `x = g(x)`, then keep plugging in values until x stops changing.**

---

## 🔁 What is a "Fixed Point"?

A **fixed point** is a value that, when you put it into a function, you get the **same value back**.

```
x = g(x)
```

Think of it like a mirror reflecting itself. If you feed the output back as input, it stays the same.

### Example

If `g(x) = cos(x)`, try:
- `g(0.739) ≈ 0.739` ← This is a fixed point!

The idea: if we can rewrite our root-finding problem `f(x) = 0` into the form `x = g(x)`, then finding the **fixed point of g** is the same as **finding the root of f**.

---

## 🔄 The Algorithm

1. Rewrite `f(x) = 0` as `x = g(x)`
2. Pick an initial guess `x₀`
3. Compute `x₁ = g(x₀)`
4. Compute `x₂ = g(x₁)`
5. Keep going: `xₙ₊₁ = g(xₙ)`
6. Stop when `|xₙ₊₁ − xₙ|` is small enough

If the sequence converges, it converges to the root!

---

## 📖 Story Example — `f(x) = 3x − cos(x) − 1`

### Scene Setup

Imagine you're trying to find a secret locker number (the root). The locker contains a clue that leads you to another locker, which leads to another, and so on — until you arrive at the locker that points back to **itself**. That locker is the answer.

### Step 1: Rearrange into `x = g(x)`

Start with:
```
3x − cos(x) − 1 = 0
```

Add `cos(x) + 1` to both sides:
```
3x = cos(x) + 1
```

Divide by 3:
```
x = (cos(x) + 1) / 3
```

So:
```
g(x) = (cos(x) + 1) / 3
```

This is our iteration formula. Every time we compute `g(x)`, we get a new `x` that's hopefully closer to the root.

### Step 2: Choose Initial Guess

Let `x₀ = 0`

---

### Iteration 1

```
x₁ = g(x₀) = g(0) = (cos(0) + 1) / 3
            = (1 + 1) / 3
            = 2 / 3
            = 0.6667
```

We go from `0` to `0.6667` in one step. Already much closer to the root!

---

### Iteration 2

```
x₂ = g(x₁) = g(0.6667) = (cos(0.6667) + 1) / 3

cos(0.6667) ≈ 0.7860

x₂ = (0.7860 + 1) / 3
   = 1.7860 / 3
   = 0.5953
```

---

### Iteration 3

```
x₃ = g(0.5953) = (cos(0.5953) + 1) / 3

cos(0.5953) ≈ 0.8280

x₃ = (0.8280 + 1) / 3 = 0.6093
```

---

### Watching Convergence

| Iteration | xₙ |
|---|---|
| 0 | 0.0000 |
| 1 | 0.6667 |
| 2 | 0.5953 |
| 3 | 0.6093 |
| 4 | 0.6067 |
| 5 | 0.6072 |

The values are **bouncing around but getting closer** to ≈ 0.607. This is convergence in action — like a pendulum slowly settling.

### ✅ Final Answer: `x ≈ 0.607102`

---

## 🐍 Python Code

```python
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
```

### Output

```
Iteration    Root Approximation
1            0.666667
2            0.595296
3            0.609328
4            0.606678
5            0.607182

Approximate root = 0.607182
```

---

## ⚠️ When Does It Work? The Convergence Condition

Fixed Point Iteration doesn't always work. It **converges** only when:

```
|g'(x)| < 1   near the root
```

In plain English: the slope of `g(x)` must be **less than 1** near the root. If the slope is too steep, the iterations will **diverge** (shoot off to infinity) instead of converging.

For our `g(x) = (cos(x) + 1) / 3`:
```
g'(x) = −sin(x) / 3

At x ≈ 0.607:
g'(0.607) = −sin(0.607) / 3 ≈ −0.569 / 3 ≈ −0.19
```

`|−0.19| = 0.19 < 1` ✅ — Convergence is guaranteed.

---

## 🎯 Key Takeaways

- Fixed Point Iteration rewrites `f(x) = 0` as `x = g(x)`, then repeatedly computes `xₙ₊₁ = g(xₙ)`.
- It works like following a trail of clues that leads back to itself.
- Convergence depends on `|g'(x)| < 1` — if the slope is too steep, it blows up.
- The **same equation can have multiple valid rearrangements** — some converge, some don't. You have to choose wisely!
- Real root for `f(x) = 3x − cos(x) − 1`: **x ≈ 0.607102**
