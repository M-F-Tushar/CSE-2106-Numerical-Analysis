# The Regula Falsi Method
## (Also Called: False Position Method)

---

## 🧠 The Problem with Bisection

The Bisection Method works great, but it has one annoying flaw: **it's dumb about where the root probably is.**

Imagine looking for a treasure between mile 0 and mile 1. You always check mile 0.5 — the dead center — even if all the clues suggest the treasure is near mile 0.9.

**Regula Falsi says:** *"Why not be smarter? Use the values of the function to make a better guess!"*

---

## 🔍 The Big Idea

Instead of cutting the interval at the **midpoint**, Regula Falsi draws a **straight line** (a secant line) between the two points `(a, f(a))` and `(b, f(b))`, and finds where that line **crosses zero**.

That crossing point is likely much closer to the actual root than the simple midpoint.

This is why it's called "False Position" — you're using the position where a straight line *falsely* (approximately) hits zero.

---

## 📐 The Formula

If `a` and `b` are your two boundary points with `f(a) × f(b) < 0`, the next guess `x` is:

```
x = (a·f(b) − b·f(a)) / (f(b) − f(a))
```

Think of this as the **x-intercept of the line** connecting `(a, f(a))` and `(b, f(b))`.

After computing `x`:
- If `f(a) × f(x) < 0` → root is between `a` and `x` → set `b = x`
- Otherwise → root is between `x` and `b` → set `a = x`

---

## 📖 Story Example — Same Function `f(x) = 3x − cos(x) − 1`

### Scene Setup

You're a clever treasure hunter. You know the treasure is between mile 0 and mile 1. But this time, instead of just going to the middle, you **draw a line between your two clue readings** and walk to where that line hits the road level.

### Step 1: Confirm the interval

```
f(0) = 3(0) − cos(0) − 1 = −1 − 1 = −2
f(1) = 3(1) − cos(1) − 1 ≈ 3 − 0.5403 − 1 = 1.4597
```

`f(0) × f(1) < 0` ✅ — Root lies between 0 and 1.

---

### Iteration 1

```
a = 0,   b = 1
f(a) = −2,   f(b) = 1.4597

x₁ = (0 × 1.4597 − 1 × (−2)) / (1.4597 − (−2))
   = (0 + 2) / 3.4597
   = 2 / 3.4597
   = 0.5781
```

Now evaluate:
```
f(0.5781) = 3(0.5781) − cos(0.5781) − 1
          = 1.7343 − 0.8372 − 1
          = −0.1029   ← negative
```

Since `f(0.5781)` is negative (same sign as `f(a)`), replace `a = 0.5781`.

---

### Iteration 2

```
a = 0.5781,   b = 1
f(a) = −0.1029,   f(b) = 1.4597

x₂ = (0.5781 × 1.4597 − 1 × (−0.1029)) / (1.4597 − (−0.1029))
   = (0.8436 + 0.1029) / 1.5626
   = 0.9465 / 1.5626
   = 0.6058
```

```
f(0.6058) = 3(0.6058) − cos(0.6058) − 1
          = 1.8174 − 0.8220 − 1
          = −0.0046   ← negative (but much smaller!)
```

Still negative → replace `a = 0.6058`.

---

### Iteration 3

```
a = 0.6058,   b = 1
f(a) = −0.0046,   f(b) = 1.4597

x₃ = (0.6058 × 1.4597 − 1 × (−0.0046)) / (1.4597 − (−0.0046))
   = (0.8842 + 0.0046) / 1.4643
   = 0.8888 / 1.4643
   = 0.6067
```

```
f(0.6067) = 1.8201 − 0.8214 − 1 = −0.0013 ≈ 0
```

### ✅ Final Answer: `x ≈ 0.607`

---

## 📊 Convergence Comparison

Notice how quickly Regula Falsi homes in:

| Iteration | Root Approximation |
|---|---|
| 1 | 0.5781 |
| 2 | 0.6058 |
| 3 | 0.6067 → converged! |

Compare this to Bisection which took **8+ iterations** to reach similar precision. Regula Falsi is smarter!

---

## 🐍 Python Code

```python
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
```

### Output

```
Iteration    Root Approximation
1            0.578085
2            0.605959
3            0.607057
4            0.607100
5            0.607102

Approximate root = 0.607102
```

---

## ⚖️ Regula Falsi vs Bisection

| Feature | Bisection | Regula Falsi |
|---|---|---|
| Strategy | Always use midpoint | Use smart line intersection |
| Speed | Slower | Usually faster |
| Guaranteed convergence | Yes | Yes (with opposite signs) |
| Needs derivative? | No | No |
| Always one-sided? | No | Sometimes gets "stuck" on one side |

> ⚠️ One weakness: Regula Falsi can sometimes get **stuck updating only one end** of the interval, making it slower in certain edge cases. This was addressed by the "Illinois method" (a modification of Regula Falsi).

---

## 🎯 Key Takeaways

- Regula Falsi is a **smarter Bisection** — it uses the function values to estimate where the root is, rather than blindly taking the midpoint.
- The formula draws a **line between two points** and finds where it crosses zero.
- It keeps the two points on **opposite sides** of the root at all times.
- Real root for `f(x) = 3x − cos(x) − 1`: **x ≈ 0.607102**
