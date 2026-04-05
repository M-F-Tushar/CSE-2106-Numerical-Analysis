# The Bisection Method
## Finding Roots by Cutting the Problem in Half
---

## 🧠 What is a "Root"?

Before we talk about the method, let's understand what we're looking for.

A **root** (also called a *zero*) of a function `f(x)` is an `x` value that makes the function equal to zero:

```
f(x) = 0
```

### Simple Example

For `f(x) = x² − 4`:

```
x² − 4 = 0
x² = 4
x = ±2
```

The roots are `x = -2` and `x = 2`. Easy enough when we can solve by hand. But what about a messy equation like `f(x) = 3x − cos(x) − 1`? You can't rearrange that into a neat answer. That's where **numerical methods** come in.

---

## 🔍 The Big Idea Behind Bisection

Think about a game of **"Hot or Cold"**.

You're looking for a hidden object in a room. Your friend says:
- "You're cold" when you're far away
- "You're hot" when you're close

The Bisection Method works like this — but instead of temperature, it uses the **sign of the function** (positive or negative).

### The Key Insight

If `f(a)` is **negative** and `f(b)` is **positive**, then somewhere between `a` and `b`, the function must have **crossed zero**. That crossing point is the root.

```
f(a) × f(b) < 0  →  a root exists between a and b
```

This is guaranteed by the **Intermediate Value Theorem** in mathematics.

---

## 🎯 The Strategy: Keep Cutting in Half

Once you know the root is between `a` and `b`, you:

1. Find the **midpoint** `c = (a + b) / 2`
2. Check `f(c)`:
   - If `f(c) = 0` → You found the root! Done.
   - If `f(a) × f(c) < 0` → Root is in the **left half** → Set `b = c`
   - Otherwise → Root is in the **right half** → Set `a = c`
3. Repeat until the interval is tiny enough (below your tolerance)

Each step literally **cuts the search interval in half** — hence the name "Bisection."

---

## 📖 Worked Example — `f(x) = 3x − cos(x) − 1`

### Step 1: Check the Endpoints

```
f(0) = 3(0) − cos(0) − 1 = 0 − 1 − 1 = −2        ← negative
f(1) = 3(1) − cos(1) − 1 ≈ 3 − 0.5403 − 1 = 1.4597  ← positive
```

`f(0) × f(1) < 0` ✅ — Root confirmed between 0 and 1.

---

### Step 2: Start Bisecting

**Iteration 1:**
```
a = 0,  b = 1
c = (0 + 1) / 2 = 0.5

f(0.5) = 3(0.5) − cos(0.5) − 1
       = 1.5 − 0.8776 − 1
       = −0.3776   ← negative

f(0) × f(0.5) = (−2) × (−0.3776) > 0  → Root in RIGHT half → set a = 0.5
```

---

**Iteration 2:**
```
a = 0.5,  b = 1
c = (0.5 + 1) / 2 = 0.75

f(0.75) = 3(0.75) − cos(0.75) − 1
        = 2.25 − 0.7317 − 1
        = 0.5183   ← positive   ✅ CORRECTED (was 0.4746)
```
Root is in the **left half** (between 0.5 and 0.75) → set `b = 0.75`

---

**Iteration 3:**
```
a = 0.5,  b = 0.75
c = 0.625

f(0.625) = 3(0.625) − cos(0.625) − 1
         = 1.875 − 0.8108 − 1
         = 0.0640   ← positive   ✅ CORRECTED (was 0.2220)
```
Root is in the **left half** (between 0.5 and 0.625) → set `b = 0.625`

---

### Full Iteration Table ✅ (All Corrected)

> ⚠️ **Note:** The original table had wrong `f(c)` values in every row. From iteration 4 onward, the `a` and `b` columns were also incorrect — the table never properly updated the bracket. The corrected table is below.

| Iteration | a        | b        | c        | f(c)    | Action            |
|-----------|----------|----------|----------|---------|-------------------|
| 1         | 0        | 1        | 0.500000 | −0.3776 | a = 0.5 (right)   |
| 2         | 0.5      | 1        | 0.750000 | +0.5183 | b = 0.75 (left)   |
| 3         | 0.5      | 0.75     | 0.625000 | +0.0640 | b = 0.625 (left)  |
| 4         | 0.5      | 0.625    | 0.562500 | −0.1584 | a = 0.5625 (right)|
| 5         | 0.5625   | 0.625    | 0.593750 | −0.0476 | a = 0.59375 (right)|
| 6         | 0.59375  | 0.625    | 0.609375 | +0.0081 | b = 0.609375 (left)|
| 7         | 0.59375  | 0.609375 | 0.601563 | −0.0198 | a = 0.601563 (right)|
| 8         | 0.601563 | 0.609375 | 0.605469 | −0.0058 | a = 0.605469 (right)|

…continuing until `|f(c)| < 1e-6`

### ✅ Final Answer: `x ≈ 0.607102`

Verified: `f(0.607102) ≈ 0.0000013 ≈ 0` ✓

---

## 🐍 Python Code

```python
import math

# Define the function f(x) = 3x - cos(x) - 1
def f(x):
    return 3*x - math.cos(x) - 1

def bisection(a, b, tolerance=1e-6, max_iterations=50):
    # Check that signs are opposite — root must exist in [a, b]
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    print(f"{'Iteration':<12} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12}")

    c = None
    for i in range(1, max_iterations + 1):
        # Find midpoint
        c = (a + b) / 2
        print(f"{i:<12} {a:<12.6f} {b:<12.6f} {c:<12.6f} {f(c):<12.6f}")

        # Stop if close enough to zero
        if abs(f(c)) < tolerance:
            print("\nRoot found within tolerance.")
            return c

        # Update interval — keep the half where sign changes
        if f(a) * f(c) < 0:
            b = c   # root in left half
        else:
            a = c   # root in right half

    print("\nMaximum iterations reached.")
    return c

# Run the method
root = bisection(a=0, b=1)
print(f"\nApproximate Root = {root:.6f}")
```

---

## ✅ Pros and ❌ Cons

| ✅ Pros | ❌ Cons |
|---|---|
| Always converges (if signs differ) | Slow — halves the interval each time |
| Very simple and reliable | Needs two initial guesses with opposite signs |
| No derivative needed | Can't find roots where function doesn't cross zero |

---

## 📌 Final Revision — Everything You Need to Remember

*A complete, step-by-step mental checklist. Read this before attempting any bisection problem.*

---

### Phase 0 — Understand What You're Doing

**Goal:** Find an `x` value such that `f(x) = 0`. This `x` is called a *root* or *zero* of the function.

You use bisection when you *cannot* solve `f(x) = 0` algebraically — for example when the equation mixes polynomials and trig like `3x − cos(x) − 1 = 0`.

---

### Phase 1 — Pick a Valid Bracket `[a, b]`

**Rule:** You need two starting points `a` and `b` such that `f(a)` and `f(b)` have *opposite signs*.

**Check:**
```
f(a) × f(b) < 0
```

- If **true** → a root is guaranteed to exist between `a` and `b` (by the Intermediate Value Theorem).
- If **false** → the method cannot start. Pick different values.

**Example for this problem:**
```
f(0) = −2        (negative)
f(1) = 1.4597    (positive)
f(0) × f(1) < 0  ✅  →  valid bracket is [0, 1]
```

---

### Phase 2 — The Core Loop (Repeat Until Done)

**Step A — Compute the midpoint:**
```
c = (a + b) / 2
```

**Step B — Evaluate the function at the midpoint:**

Compute `f(c)`. Plug `c` into your function carefully — arithmetic errors are common here. Make sure trig functions use **radians**, not degrees.

**Step C — Check if you're done:**

Stop if any of these are true:
- `f(c) = 0` exactly (rare in practice)
- `|f(c)| < tolerance` (e.g., `1e-6`) — function value close enough to zero
- `(b − a) < tolerance` — interval is tiny enough
- Maximum number of iterations reached

**Step D — Narrow the bracket (the most important step!):**

Ask: does the sign change happen in the *left half* or the *right half*?

```
Compute  f(a) × f(c)

If NEGATIVE  →  signs of f(a) and f(c) are opposite
             →  root is in LEFT half [a, c]
             →  set b = c

If POSITIVE  →  signs of f(a) and f(c) are the same
             →  root is in RIGHT half [c, b]
             →  set a = c
```

> ⚠️ **Common mistake:** After every iteration, one of `a` or `b` must change. If both stayed the same, you made an error.

**Step E — Go back to Step A** with the new (smaller) interval.

---

### Phase 3 — Track the Iteration Table Correctly

Every iteration, record: `a`, `b`, `c`, `f(c)`, and which half you kept.

| Iteration | a        | b        | c        | f(c)    | Action             |
|-----------|----------|----------|----------|---------|--------------------|
| 1         | 0        | 1        | 0.5      | −0.3776 | a = 0.5            |
| 2         | 0.5      | 1        | 0.75     | +0.5183 | b = 0.75           |
| 3         | 0.5      | 0.75     | 0.625    | +0.0640 | b = 0.625          |
| 4         | 0.5      | 0.625    | 0.5625   | −0.1584 | a = 0.5625         |
| 5         | 0.5625   | 0.625    | 0.59375  | −0.0476 | a = 0.59375        |
| 6         | 0.59375  | 0.625    | 0.609375 | +0.0081 | b = 0.609375       |
| 7         | 0.59375  | 0.609375 | 0.601563 | −0.0198 | a = 0.601563       |
| 8         | 0.601563 | 0.609375 | 0.605469 | −0.0058 | a = 0.605469       |

Notice how **both `a` and `b` change** across iterations — the interval steadily closes in on the root from both sides.

---

### Phase 4 — Common Mistakes to Avoid

1. **Forgetting to verify opposite signs first.** Always confirm `f(a) × f(b) < 0` before starting.

2. **Mixing up which half to keep.** The root is always in the half where the sign *changes* — where `f` is positive on one end and negative on the other.

3. **Freezing `a` or `b` when it should update.** Each iteration updates exactly one of `a` or `b`. If your table shows the same value for too many consecutive rows, recheck your sign logic.

4. **Arithmetic errors in `f(c)`.** For trig functions, make sure you're working in **radians**. A degree/radian mix-up will give completely wrong `f(c)` values.

5. **Using the wrong stopping criterion.** Checking `|b − a| < tol` (interval width) is different from checking `|f(c)| < tol` (function value). Both are valid — just be consistent.

---

### Phase 5 — One-Page Quick Reference

```
1. Define your function
   f(x) = 3x − cos(x) − 1

2. Find a valid bracket
   Find a, b  such that  f(a) × f(b) < 0

3. Core loop — repeat until converged:
   c = (a + b) / 2
   if |f(c)| < tolerance  →  STOP, root = c
   if f(a) × f(c) < 0     →  b = c   (root in left half)
   else                   →  a = c   (root in right half)

4. Report the root
   x ≈ 0.607102  (for this problem)

5. Verify by substituting back
   f(0.607102) ≈ 0  ✓
```

---

> The bisection method is slow — each step only halves the error — but it is the most *reliable* root-finding method available. If you bracket correctly, it will always converge. Use it when reliability matters more than speed.
