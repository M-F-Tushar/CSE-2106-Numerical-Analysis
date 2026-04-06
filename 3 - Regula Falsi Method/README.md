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

### Step 1: Confirm the Interval

```
f(0) = 3(0) − cos(0) − 1 = 0 − 1 − 1 = −2
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
          = 1.7343 − 0.8375 − 1
          = −0.1032   ← negative   ✅ CORRECTED (cos was 0.8372, f(x) was −0.1029)
```

Since `f(0.5781)` is negative (same sign as `f(a)`), replace `a = 0.5781`.

---

### Iteration 2

```
a = 0.5781,   b = 1
f(a) = −0.1032,   f(b) = 1.4597

x₂ = (0.5781 × 1.4597 − 1 × (−0.1032)) / (1.4597 − (−0.1032))
   = (0.8439 + 0.1032) / 1.5629
   = 0.9471 / 1.5629
   = 0.6060
```

> ✅ **Corrected:** `0.5781 × 1.4597 = 0.8439` (not `0.8436`). Numerator is `0.9471` (not `0.9465`), giving `x₂ = 0.6060` (not `0.6058`).

```
f(0.6060) = 3(0.6060) − cos(0.6060) − 1
          = 1.8180 − 0.8220 − 1
          = −0.0040   ← negative (much smaller!)
```

Still negative → replace `a = 0.6060`.

---

### Iteration 3

```
a = 0.6060,   b = 1
f(a) = −0.0041,   f(b) = 1.4597

x₃ = (0.6060 × 1.4597 − 1 × (−0.0041)) / (1.4597 − (−0.0041))
   = (0.8846 + 0.0041) / 1.4638
   = 0.8887 / 1.4638
   = 0.6071
```

> ✅ **Corrected:** Division gives `0.6071` (not `0.6067`). The original document also used a wrong denominator and wrong intermediate values carried from iteration 2.

```
f(0.6071) = 3(0.6071) − cos(0.6071) − 1
          = 1.8213 − 0.8213 − 1
          = −0.0002 ≈ 0
```

### ✅ Final Answer: `x ≈ 0.607102`

---

## 📊 Convergence Comparison

Notice how quickly Regula Falsi homes in:

| Iteration | Root Approximation |
|---|---|
| 1 | 0.5781 |
| 2 | 0.6060 ✅ (was 0.6058) |
| 3 | 0.6071 → converged! ✅ (was 0.6067) |

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

---

## 📌 Final Revision — Everything You Need to Remember

*A complete, step-by-step mental checklist. Read this before attempting any Regula Falsi problem.*

---

### Phase 0 — Understand What You're Doing

**Goal:** Find an `x` such that `f(x) = 0` — same goal as Bisection.

**The key difference from Bisection:** Instead of splitting the interval at its geometric center (midpoint), Regula Falsi splits it at the point where a **straight line drawn between the two endpoints** crosses zero. This tends to put the guess much closer to the actual root, especially when the function is steeply sloped on one side.

**When to use it:** When you can't solve `f(x) = 0` algebraically, you have a valid bracket `[a, b]`, and you want faster convergence than Bisection.

---

### Phase 1 — Pick a Valid Bracket `[a, b]`

**Same rule as Bisection:**

```
f(a) × f(b) < 0
```

Both signs must be opposite — this guarantees a root exists in between (by the Intermediate Value Theorem).

**Example:**
```
f(0) = −2      (negative)
f(1) = 1.4597  (positive)
f(0) × f(1) < 0  ✅  →  valid bracket is [0, 1]
```

---

### Phase 2 — The Core Formula

The new guess `x` is the x-intercept of the straight line through `(a, f(a))` and `(b, f(b))`:

```
x = (a·f(b) − b·f(a)) / (f(b) − f(a))
```

**How to remember it:** Think of it as a weighted average — the endpoint whose `f` value is closer to zero gets more weight. The formula naturally pulls the guess toward where the function is smallest.

**Step-by-step to apply the formula:**
1. Compute `f(a)` and `f(b)` (or use previously stored values)
2. Compute the numerator: `a × f(b) − b × f(a)`
3. Compute the denominator: `f(b) − f(a)`
4. Divide: `x = numerator / denominator`
5. Compute `f(x)`

> ⚠️ **Common arithmetic mistake:** In the numerator, you are subtracting `b × f(a)` — be careful with signs when `f(a)` is negative. A negative times a negative becomes positive. Double-check each multiplication before subtracting.

---

### Phase 3 — Update the Bracket

Exactly the same logic as Bisection:

```
Compute  f(a) × f(x)

If NEGATIVE  →  signs of f(a) and f(x) differ
             →  root is between a and x (left side)
             →  set b = x

If POSITIVE  →  signs of f(a) and f(x) are the same
             →  root is between x and b (right side)
             →  set a = x
```

After updating, go back to Phase 2 with the new `a` or `b`.

> ⚠️ **One-sided sticking:** In Regula Falsi, one endpoint often never moves. In the example above, `b` stays at 1.0 for all five iterations — only `a` ever updates. This is normal behavior, not a mistake. It becomes a problem only in extreme cases (the "Illinois method" fixes this).

---

### Phase 4 — Full Worked Example at a Glance

| Iter | a        | b   | f(a)     | f(b)   | x        | f(x)     | Update    |
|------|----------|-----|----------|--------|----------|----------|-----------|
| 1    | 0        | 1   | −2.0000  | 1.4597 | 0.578085 | −0.1033  | a = 0.5781|
| 2    | 0.578085 | 1   | −0.1033  | 1.4597 | 0.605959 | −0.0041  | a = 0.6060|
| 3    | 0.605959 | 1   | −0.0041  | 1.4597 | 0.607057 | −0.0002  | a = 0.6071|
| 4    | 0.607057 | 1   | −0.0002  | 1.4597 | 0.607100 | −0.000006| a = 0.6071|
| 5    | 0.607100 | 1   | −0.000006| 1.4597 | 0.607102 | ≈ 0      | done ✅   |

Notice that `b = 1` never changes — the root is always found to be in the right portion `[x, b]`, so only `a` moves.

---

### Phase 5 — Stopping Conditions

Stop when any of these are satisfied:

- `|f(x)| < tolerance` (e.g., `1e-6`) — function value is close enough to zero
- `|b − a| < tolerance` — interval is narrow enough
- `f(x) = 0` exactly (rare)
- Maximum number of iterations reached

---

### Phase 6 — Common Mistakes to Avoid

1. **Sign errors in the numerator.** The formula involves `a × f(b) − b × f(a)`. When `f(a)` is negative, `−b × f(a)` becomes positive. Write each term out fully before combining.

2. **Forgetting to use the stored f values.** In each iteration you already have `f(a)` from the previous step — don't recompute it. Use the stored value to avoid rounding drift.

3. **Wrong update rule.** As with Bisection, check `f(a) × f(x)` — not `f(b) × f(x)` — to decide which side the root is on.

4. **Expecting both endpoints to move.** In many problems, one endpoint is fixed for every iteration. This is expected behavior.

5. **Using degrees instead of radians.** For any trig in `f(x)`, always use radians. `cos(0.578)` in degrees gives a completely different number.

---

### Phase 7 — Regula Falsi vs Bisection Quick Comparison

| | Bisection | Regula Falsi |
|---|---|---|
| Guess formula | `c = (a + b) / 2` | `x = (a·f(b) − b·f(a)) / (f(b) − f(a))` |
| Uses function values? | No | Yes |
| Speed | Slower (halves interval mechanically) | Usually faster (weighted toward root) |
| One endpoint stuck? | Never | Often (normal) |
| Derivative needed? | No | No |
| Always converges? | Yes (if bracket valid) | Yes (if bracket valid) |

---

### Phase 8 — One-Page Quick Reference

```
1. Define your function
   f(x) = 3x − cos(x) − 1

2. Find a valid bracket
   Find a, b  such that  f(a) × f(b) < 0

3. Core loop — repeat until converged:

   x = (a·f(b) − b·f(a)) / (f(b) − f(a))

   if |f(x)| < tolerance  →  STOP, root = x
   if f(a) × f(x) < 0     →  b = x   (root in left side)
   else                   →  a = x   (root in right side)

4. Report the root
   x ≈ 0.607102  (for this problem)

5. Verify by substituting back
   f(0.607102) ≈ 0  ✓
```

---

> Regula Falsi is faster than Bisection in most cases because it uses the *shape* of the function, not just the *size* of the interval. However, it can stall when one endpoint gets stuck far from the root. For those edge cases, consider the **Illinois Method** — a small modification that prevents one-sided sticking.
