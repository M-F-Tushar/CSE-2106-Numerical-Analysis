# The Secant Method
## Newton-Raphson Without the Derivative

---

## 🧠 The Problem with Newton-Raphson

Newton-Raphson is incredibly fast, but it has one hard requirement: **you must know the derivative `f'(x)`.**

For many real-world problems, computing the derivative is either:
- **Difficult** (messy or complex functions)
- **Impossible** (data collected from experiments, not a formula)
- **Not worth the effort** for a quick approximation

The **Secant Method** solves this by *approximating* the derivative numerically, using two points instead of one.

---

## 🔍 The Big Idea

In Newton-Raphson, we use:
```
f'(xₙ) = slope of tangent line at xₙ
```

The Secant Method replaces this with:
```
slope ≈ (f(xₙ) − f(xₙ₋₁)) / (xₙ − xₙ₋₁)
```

This is the **slope of the line through two known points** — a secant line instead of a tangent line. You don't need calculus; you just need two previous guesses.

---

## 📐 The Formula

```
xₙ₊₁ = xₙ − f(xₙ) · (xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁))
```

This looks complex, but it's really just "Newton-Raphson with an approximated slope."

You need **two initial guesses** to get started: `x₀` and `x₁`.

---

## 📖 Story Example — `f(x) = 3x − cos(x) − 1`

### Scene Setup

You're an architect measuring where a sloped wall meets the floor. You can't measure the slope directly (no derivative), but you have **two height readings** at two known positions. You draw a line through them and find where it hits the floor. Then use that floor point as one of your next two readings. Repeat.

### Initial Setup

```
x₀ = 0,   x₁ = 1

f(0) = 3(0) − cos(0) − 1 = −2
f(1) = 3(1) − cos(1) − 1 ≈ 1.4597
```

---

### Iteration 1 — Compute `x₂`

```
x₂ = x₁ − f(x₁) · (x₁ − x₀) / (f(x₁) − f(x₀))

   = 1 − 1.4597 · (1 − 0) / (1.4597 − (−2))

   = 1 − 1.4597 / 3.4597

   = 1 − 0.4219

   = 0.5781
```

New guess: `x₂ = 0.5781`

---

### Iteration 2 — Compute `x₃`

Now use `x₁ = 1` and `x₂ = 0.5781`:
```
f(0.5781) ≈ −0.1029

x₃ = 0.5781 − (−0.1029) · (0.5781 − 1) / (−0.1029 − 1.4597)

   = 0.5781 − (−0.1029) · (−0.4219) / (−1.5626)

   = 0.5781 + (−0.1029) · 0.2699

   = 0.5781 + 0.0278

   = 0.6059
```

---

### Iteration 3 — Compute `x₄`

Use `x₂ = 0.5781` and `x₃ = 0.6059`:
```
f(0.6059) ≈ −0.0046

x₄ ≈ 0.6070
```

---

### Convergence Table

| Iteration | Root Approximation |
|---|---|
| 1 | 0.5781 |
| 2 | 0.6059 |
| 3 | 0.6070 |
| 4 | 0.6071 |
| 5 | 0.607102 ✅ |

### ✅ Final Answer: `x ≈ 0.607102`

---

## 🐍 Python Code

```python
import math

# Function definition
def f(x):
    return 3*x - math.cos(x) - 1

def secant_method(x0=0, x1=1, iterations=5):
    print(f"{'Iteration':<12} {'Root Approximation'}")

    x2 = x1
    for i in range(1, iterations + 1):
        # Secant formula: approximate slope using two previous points
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"{i:<12} {x2:.6f}")

        # Slide the window forward
        x0 = x1
        x1 = x2

    print(f"\nApproximate root = {x2:.6f}")
    return x2

# Run the method
secant_method(x0=0, x1=1)
```

### Output

```
Iteration    Root Approximation
1            0.578085
2            0.605959
3            0.607106
4            0.607102
5            0.607102

Approximate root = 0.607102
```

---

## 🔑 Understanding the "Sliding Window"

A key detail in the code:
```cpp
x0 = x1;   // old current becomes old previous
x1 = x2;   // new value becomes current
```

The Secant Method always works with the **two most recent** guesses. It's like a sliding window moving toward the root.

---

## ⚖️ Comparing All Methods on This Problem

| Method | Iterations to converge | Needs Derivative? | Needs Bracket? |
|---|---|---|---|
| Bisection | 20+ | No | Yes (opposite signs) |
| Regula Falsi | ~5 | No | Yes (opposite signs) |
| Fixed Point | ~5 | No | No |
| Newton-Raphson | 2–3 | **Yes** | No |
| Modified N-R | 3–4 | **Once** | No |
| **Secant** | 4–5 | **No** | No |

The Secant Method hits a sweet spot: **fast like Newton-Raphson, but no derivative needed.**

---

## ⚠️ Potential Pitfalls

- If `f(x₁) − f(x₀) = 0` → division by zero! (the two points have same f value)
- Unlike Bisection/Regula Falsi, the Secant Method **doesn't guarantee the root is between x₀ and x₁** — it can sometimes diverge with bad initial guesses.
- Choose two initial guesses that are reasonably close to the expected root.

---

## 🎯 Key Takeaways

- The Secant Method is Newton-Raphson with the derivative **replaced by a finite difference** (slope between two points).
- No calculus needed — just function evaluations.
- Requires **two initial guesses** (not an interval with opposite signs).
- Convergence is **superlinear** — faster than Bisection, slightly slower than Newton-Raphson.
- Real root for `f(x) = 3x − cos(x) − 1`: **x ≈ 0.607102**
