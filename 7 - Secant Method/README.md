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

### Iteration 2 — Compute `x₃` ✏️ *(corrected)*

Now use `x₁ = 1` and `x₂ = 0.5781`:
```
f(0.5781) ≈ −0.1033

x₃ = x₂ − f(x₂) · (x₂ − x₁) / (f(x₂) − f(x₁))

   = 0.5781 − (−0.1033) · (0.5781 − 1) / (−0.1033 − 1.4597)

   = 0.5781 − (−0.1033) · (−0.4219) / (−1.5630)

   = 0.5781 − (−0.1033) · 0.2699

   = 0.5781 − (−0.0279)

   = 0.5781 + 0.0279

   = 0.6060
```

> ⚠️ **Correction note:** The original document wrote the final arithmetic as
> `x₃ = 0.5781 + (−0.1029) · 0.2699 = 0.5781 + 0.0278`, which incorrectly
> treated `f(x₂) · ratio` as a positive addition directly. The correct
> result of `−f(x₂) · ratio` is `+0.0279` (subtracting a negative),
> giving `x₃ ≈ 0.6060`. The rounded f(x₂) value also slightly differs:
> it is **−0.1033**, not −0.1029.

---

### Iteration 3 — Compute `x₄`

Use `x₂ = 0.5781` and `x₃ = 0.6060`:
```
f(0.6060) ≈ −0.0041

x₄ ≈ 0.6071
```

---

### Convergence Table

| Iteration | Root Approximation |
|---|---|
| 1 | 0.5781 |
| 2 | 0.6060 |
| 3 | 0.6071 |
| 4 | 0.607102 |
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

---

---

## 📋 Final Revision Section — Everything You Need to Implement the Secant Method

This section is your complete, step-by-step implementation guide. Read this alone and you will know exactly what to do.

---

### STEP 0 — Understand What You're Solving

You have a function `f(x)` and you want to find a value of `x` such that `f(x) = 0` (called the **root**).

You **cannot or do not want** to compute the derivative `f'(x)`. That is the only reason you use the Secant Method instead of Newton-Raphson.

---

### STEP 1 — Write Down Your Function

Be precise. Evaluate it by hand at a couple of points to make sure it is correct.

**Example:**
```
f(x) = 3x − cos(x) − 1
f(0) = 0 − 1 − 1 = −2       ← negative
f(1) = 3 − cos(1) − 1 ≈ 1.4597  ← positive
```

The sign change tells you a root exists somewhere between 0 and 1. This is a good sign that your initial guesses are reasonable.

---

### STEP 2 — Choose Two Initial Guesses: `x₀` and `x₁`

You need **exactly two starting values**, not one, not an interval with a sign condition.

**Rules for choosing them:**
- They should be reasonably close to where you expect the root to be.
- They do **not** need to bracket the root (opposite signs are not required).
- They must **not** produce `f(x₁) = f(x₀)`, because that causes division by zero.
- When in doubt, pick one slightly below and one slightly above your expected root.

**Example:** `x₀ = 0`, `x₁ = 1`

---

### STEP 3 — Apply the Secant Formula Repeatedly

The core formula is:

```
x_new = x_current − f(x_current) · (x_current − x_previous) / (f(x_current) − f(x_previous))
```

Or in subscript notation:

```
xₙ₊₁ = xₙ − f(xₙ) · (xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁))
```

**Every single iteration, do this in order:**

1. Compute `f(x_current)` and `f(x_previous)` — these are just function evaluations.
2. Compute the difference `(x_current − x_previous)`.
3. Compute the difference `(f(x_current) − f(x_previous))` — this is the denominator.
4. Check: if the denominator is zero or nearly zero, **stop** — the method has failed for these guesses.
5. Divide step 2 by step 3.
6. Multiply by `f(x_current)`.
7. Subtract the result from `x_current` to get `x_new`.
8. **Slide the window:** `x_previous ← x_current`, then `x_current ← x_new`.

---

### STEP 4 — Work Through the First Two Iterations by Hand

This is the most important practice step. If you can do two iterations cleanly by hand, you understand the method.

**Iteration 1** (using `x₀ = 0`, `x₁ = 1`):
```
x₂ = 1 − f(1) · (1 − 0) / (f(1) − f(0))
   = 1 − 1.4597 · 1 / (1.4597 − (−2))
   = 1 − 1.4597 / 3.4597
   = 1 − 0.4219
   = 0.5781
```

**Iteration 2** (now using `x₁ = 1` as previous, `x₂ = 0.5781` as current):
```
f(0.5781) ≈ −0.1033

x₃ = 0.5781 − (−0.1033) · (0.5781 − 1) / (−0.1033 − 1.4597)
   = 0.5781 − (−0.1033) · (−0.4219) / (−1.5630)
   = 0.5781 − (−0.1033) · 0.2699
   = 0.5781 − (−0.0279)
   = 0.5781 + 0.0279
   = 0.6060
```

**Watch out for sign errors here.** Subtracting a negative is addition. This is the most common place to make arithmetic mistakes.

---

### STEP 5 — Know When to Stop (Stopping Criteria)

You stop iterating when one of these conditions is met:

| Condition | What it means |
|---|---|
| `|f(xₙ)| < tolerance` | The function value is close enough to zero |
| `|xₙ − xₙ₋₁| < tolerance` | Two consecutive guesses are nearly identical |
| Maximum iterations reached | Safety cap to prevent infinite loops |

**Typical tolerance:** `1e-6` (i.e., 0.000001) for most textbook problems.

For this problem, convergence happens around **iteration 4–5**, giving `x ≈ 0.607102`.

---

### STEP 6 — Write the Code (Python Template)

```python
import math

def f(x):
    return 3*x - math.cos(x) - 1   # ← Replace with your own function

def secant_method(x0, x1, tol=1e-6, max_iter=50):
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)

        # Safety check: avoid division by zero
        if abs(fx1 - fx0) < 1e-12:
            print("Division by zero risk. Method failed.")
            return None

        # Core secant formula
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        print(f"Iteration {i}: x = {x2:.6f},  f(x) = {f(x2):.8f}")

        # Check stopping condition
        if abs(x2 - x1) < tol:
            print(f"\nConverged! Root ≈ {x2:.6f}")
            return x2

        # Slide the window — THIS IS CRITICAL
        x0 = x1
        x1 = x2

    print("Did not converge within max iterations.")
    return x1

# Call it
secant_method(x0=0, x1=1)
```

---

### STEP 7 — Common Mistakes to Avoid

| Mistake | Why it's wrong | Fix |
|---|---|---|
| Using only one initial guess | The method needs two | Always supply `x0` AND `x1` |
| Forgetting to slide the window | You'll keep reusing the same two points | Always do `x0 = x1; x1 = x2` after each step |
| Sign error in the formula | Subtracting a negative = adding | Write each sign explicitly and check twice |
| Not checking denominator = 0 | Causes crash or infinite value | Add `if abs(fx1 - fx0) < epsilon: stop` |
| Expecting guaranteed convergence | The method can diverge | If it diverges, pick better initial guesses |

---

### STEP 8 — Quick Mental Checklist Before You Submit / Run

```
✅ Did I define f(x) correctly and verify f(x₀) and f(x₁) by hand?
✅ Did I choose two distinct initial guesses?
✅ Is my formula  x_new = x_current − f(x_current)·(x_current − x_prev)/(f(x_current) − f(x_prev)) ?
✅ Am I sliding the window AFTER each iteration (x0 ← x1, x1 ← x2)?
✅ Did I check for sign errors, especially when f(x) is negative?
✅ Did I set a stopping condition (tolerance or max iterations)?
✅ Does my final answer satisfy f(root) ≈ 0?
```

---

### Summary in One Line

> **Pick two guesses → draw a secant line through their function values → find where that line hits zero → repeat with the newest two points → stop when close enough.**
