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
sin(0.607) ≈ 0.5705                      ✅ CORRECTED (was 0.569)
g'(0.607) = −0.5705 / 3 ≈ −0.1902
```

`|−0.1902| ≈ 0.19 < 1` ✅ — Convergence is guaranteed.

---

## 🎯 Key Takeaways

- Fixed Point Iteration rewrites `f(x) = 0` as `x = g(x)`, then repeatedly computes `xₙ₊₁ = g(xₙ)`.
- It works like following a trail of clues that leads back to itself.
- Convergence depends on `|g'(x)| < 1` — if the slope is too steep, it blows up.
- The **same equation can have multiple valid rearrangements** — some converge, some don't. You have to choose wisely!
- Real root for `f(x) = 3x − cos(x) − 1`: **x ≈ 0.607102**

---

## 📌 Final Revision — Everything You Need to Remember

*A complete, step-by-step mental checklist. Read this before attempting any Fixed Point Iteration problem.*

---

### Phase 0 — Understand What You're Doing

**Goal:** Find `x` such that `f(x) = 0`, but using a completely different strategy from Bisection or Regula Falsi.

**Core concept:** Rewrite the equation into the form `x = g(x)`. Then starting from any guess `x₀`, repeatedly apply `x = g(x)`. If things go well, the sequence of values will converge toward the root.

**What is a fixed point?** A value `x*` where `g(x*) = x*` — the function maps the value back to itself. At that point, the iteration stops changing, and `x*` is your root.

---

### Phase 1 — Rearrange f(x) = 0 into x = g(x)

This is the most creative and most important step. There is no single mechanical way to do it — you have to use algebra.

**For `f(x) = 3x − cos(x) − 1 = 0`:**

```
3x − cos(x) − 1 = 0
3x = cos(x) + 1
x = (cos(x) + 1) / 3
```

So: `g(x) = (cos(x) + 1) / 3`

> ⚠️ **Important:** The same equation can be rearranged in multiple ways, giving different `g(x)` functions. Not all of them will converge. You must check the convergence condition (Phase 3) before committing to a rearrangement.

---

### Phase 2 — The Core Iteration Loop

**Pick a starting guess** `x₀` (any reasonable value near the expected root).

**Repeat:**
```
x₁ = g(x₀)
x₂ = g(x₁)
x₃ = g(x₂)
...
xₙ₊₁ = g(xₙ)
```

**Stop when:**
```
|xₙ₊₁ − xₙ| < tolerance     (consecutive values barely change)
```
or when a maximum iteration count is reached.

> ⚠️ **Common mistake:** People sometimes forget to update `x₀ = x₁` after each step. The new output must become the next input, or the loop does nothing.

---

### Phase 3 — Check the Convergence Condition

Before you start iterating (or after, to confirm), check:

```
|g'(x)| < 1   near the root
```

**How to compute `g'(x)`:**
Differentiate `g(x)` with respect to `x`.

For `g(x) = (cos(x) + 1) / 3`:
```
g'(x) = −sin(x) / 3
```

**Evaluate at the root:**
```
sin(0.607) ≈ 0.5705
g'(0.607) = −0.5705 / 3 ≈ −0.1902
|g'(0.607)| ≈ 0.19 < 1  ✅  →  converges
```

**If `|g'(x)| ≥ 1` near the root:** the method will diverge — each iteration moves farther away from the root. You must choose a different rearrangement of `g(x)`.

| `|g'(x)|` value | Behavior |
|---|---|
| Close to 0 | Very fast convergence |
| Between 0 and 1 | Converges (slower as it approaches 1) |
| Exactly 1 | Inconclusive — may not converge |
| Greater than 1 | Diverges — do not use this g(x) |

---

### Phase 4 — Full Worked Example at a Glance

**Function:** `f(x) = 3x − cos(x) − 1`,   **g(x) = (cos(x) + 1) / 3`,   **x₀ = 0**

| Iteration | xₙ     | g(xₙ)  |
|-----------|--------|--------|
| 0         | 0.0000 | —      |
| 1         | 0.6667 | g(0)   |
| 2         | 0.5953 | g(0.6667) |
| 3         | 0.6093 | g(0.5953) |
| 4         | 0.6067 | g(0.6093) |
| 5         | 0.6072 | g(0.6067) |

The sequence oscillates above and below the true root (0.607102) with each swing getting smaller — like a pendulum settling.

---

### Phase 5 — Stopping Conditions

Stop when any of these are met:

- `|xₙ₊₁ − xₙ| < tolerance` — consecutive guesses barely differ (most common)
- `|f(xₙ)| < tolerance` — the function value is close enough to zero
- Maximum iteration count reached

> Note: Unlike Bisection, there is **no guaranteed bracket** narrowing. You rely on the derivative condition to know you're converging, and on the stopping criterion to know when to stop.

---

### Phase 6 — Common Mistakes to Avoid

1. **Skipping the convergence check.** Always verify `|g'(x)| < 1` near the root before trusting your rearrangement. Just because an iteration produces numbers doesn't mean those numbers are converging.

2. **Not updating the input.** Every iteration, the output of `g(xₙ)` must become the new `xₙ` for the next step. If you keep feeding in the same `x₀`, you'll compute the same `x₁` forever.

3. **Choosing a bad g(x).** If your rearrangement has `|g'(x)| > 1`, the method will diverge. Try a different algebraic rearrangement of the same equation.

4. **Using degrees instead of radians.** Trig functions in numerical methods always use radians. `sin(0.607)` in degrees gives a very different value.

5. **Confusing convergence speed with correctness.** Fixed Point Iteration can be slow (the convergence table shows values bouncing: 0.6667 → 0.5953 → 0.6093 → ...). This is normal. As long as `|g'(x)| < 1`, it is converging — just be patient with the iterations.

---

### Phase 7 — Comparing Fixed Point Iteration to Previous Methods

| Feature | Bisection | Regula Falsi | Fixed Point |
|---|---|---|---|
| Requires bracket `[a,b]`? | Yes | Yes | No |
| Formula for new guess | `(a+b)/2` | Secant line x-intercept | `xₙ₊₁ = g(xₙ)` |
| Convergence guaranteed? | Yes (always) | Yes (with bracket) | Only if `\|g'(x)\| < 1` |
| Speed | Slow | Faster | Depends on `\|g'(x)\|` |
| Needs derivative? | No | No | Yes (to verify condition) |
| Requires rearrangement? | No | No | Yes — must find `g(x)` |

---

### Phase 8 — One-Page Quick Reference

```
1. Rearrange f(x) = 0  into  x = g(x)
   Example:  3x − cos(x) − 1 = 0
             →  x = (cos(x) + 1) / 3
             →  g(x) = (cos(x) + 1) / 3

2. Verify convergence:  |g'(x)| < 1  near the root
   g'(x) = −sin(x) / 3
   |g'(0.607)| = |−0.5705 / 3| ≈ 0.19 < 1  ✅

3. Choose initial guess x₀ (e.g., x₀ = 0)

4. Core loop — repeat until |xₙ₊₁ − xₙ| < tolerance:
   xₙ₊₁ = g(xₙ)

5. Report the root
   x ≈ 0.607102  (for this problem)

6. Verify:  f(0.607102) ≈ 0  ✓
```

---

> Fixed Point Iteration is elegant but fragile — it requires a smart choice of `g(x)`. If the slope of `g` is shallow (close to 0), it converges very fast. If it's close to 1, it crawls. If it exceeds 1, it fails. The method rewards careful setup but punishes blind application.
