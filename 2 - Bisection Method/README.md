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

## 📖 Story Example — Finding the Root of `f(x) = 3x − cos(x) − 1`

### Scene Setup

Imagine a mysterious treasure is buried somewhere between mile marker **0** and mile marker **1** on a long road. You have a special detector that gives a **negative reading** at mile 0 and a **positive reading** at mile 1 — so the treasure must be somewhere in between.

Your strategy: always check the **middle point**, then eliminate the half where the treasure definitely isn't.

### Step 1: Check the endpoints

```
f(0) = 3(0) − cos(0) − 1 = 0 − 1 − 1 = −2   ← negative
f(1) = 3(1) − cos(1) − 1 ≈ 3 − 0.5403 − 1 = 1.4597   ← positive
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
```
Root is in the **right half** (between 0.5 and 1) → set `a = 0.5`

---

**Iteration 2:**
```
a = 0.5,  b = 1
c = (0.5 + 1) / 2 = 0.75

f(0.75) ≈ 0.4746   ← positive
```
Root is in the **left half** (between 0.5 and 0.75) → set `b = 0.75`

---

**Iteration 3:**
```
a = 0.5,  b = 0.75
c = 0.625

f(0.625) ≈ 0.2220   ← positive
```
Root is in the **left half** (between 0.5 and 0.625) → set `b = 0.625`

---

The iterations continue, with the interval shrinking each time:

| Iteration | a | b | c | f(c) |
|---|---|---|---|---|
| 1 | 0 | 1 | 0.5 | −0.0203 |
| 2 | 0.5 | 1 | 0.75 | 0.4746 |
| 3 | 0.5 | 0.75 | 0.625 | 0.2220 |
| 4 | 0.5 | 0.625 | 0.5625 | 0.1006 |
| 5 | 0.5 | 0.5625 | 0.53125 | 0.0399 |
| 6 | 0.5 | 0.53125 | 0.51563 | 0.0098 |
| 7 | 0.5 | 0.51563 | 0.50781 | −0.0052 |
| 8 | 0.50781 | 0.51563 | 0.51172 | 0.0023 |

...continuing until `|f(c)| < 1e-6`

### ✅ Final Answer: `x ≈ 0.607102`

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

## 🎯 Key Takeaways

- Bisection is the **safest** root-finding method — it always works if you start right.
- It's **slow** but **reliable** — each iteration only cuts the error in half.
- The stopping condition is usually `|f(c)| < tolerance` or the interval width becoming tiny.
- Real root for this problem: **x ≈ 0.607102**
