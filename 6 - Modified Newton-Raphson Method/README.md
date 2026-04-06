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
f(x)  = 3x − cos(x) − 1
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
f(0.6070) = 3(0.6070) − cos(0.6070) − 1
          = 1.8210 − 0.8212 − 1
          = −0.0002

x₃ = 0.6070 − (−0.0002) / 3.4794
   = 0.6070 + 0.0000575
   = 0.6071          ← ✅ CORRECTED (original text vaguely stated 0.607 — should be 0.6071)
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

---

---

# 📋 Final Revision Section — Everything You Need to Implement Modified Newton-Raphson

> This section is your complete, self-contained implementation guide. Read this before solving any Modified Newton-Raphson problem.

---

## THE ONE KEY DIFFERENCE TO BURN INTO MEMORY

| | Standard Newton-Raphson | Modified Newton-Raphson |
|---|---|---|
| **Denominator** | `f'(xₙ)` — recomputed fresh every iteration | `f'(x₀)` — computed once, frozen forever |
| **Formula** | `xₙ₊₁ = xₙ − f(xₙ) / f'(xₙ)` | `xₙ₊₁ = xₙ − f(xₙ) / f'(x₀)` |

Everything else — the setup, the iteration table, the stopping criteria — is **identical** to standard Newton-Raphson.

---

## STEP 0 — Understand What You Are Solving

You have `f(x) = 0` and you need the root. The Modified method finds the exact same root as the standard method, just using a cheaper fixed denominator throughout.

---

## STEP 1 — Write Down f(x) and Find f'(x)

You still need the derivative — but only to evaluate it once.

```
f(x)  = given function
f'(x) = differentiate it yourself
```

Common derivative rules:

| Function term | Its derivative |
|---|---|
| constant | 0 |
| ax | a |
| xⁿ | n·xⁿ⁻¹ |
| sin(x) | cos(x) |
| cos(x) | −sin(x) |
| eˣ | eˣ |
| ln(x) | 1/x |

> ⚠️ Differentiate carefully — a wrong f'(x) corrupts your fixed denominator and poisons every single iteration.

---

## STEP 2 — Choose x₀ and Compute f'(x₀) ONCE

Pick your initial guess x₀ (the problem usually gives it).

Then compute the fixed denominator:
```
f'(x₀) = [substitute x₀ into your derivative expression]
         = [some number — call it D]
```

**Write this number D down clearly** and circle or box it. You will use it in every iteration. Do not recompute it. Do not update it.

**Safety check:** D must not be zero. If f'(x₀) = 0, choose a different x₀.

---

## STEP 3 — Apply the Fixed Formula Repeatedly

The formula for every iteration is:
```
xₙ₊₁ = xₙ − f(xₙ) / D
```

where **D never changes**.

**How to execute each iteration by hand:**

1. Plug the current xₙ into f(x) → compute f(xₙ)
2. Divide f(xₙ) by D (the fixed number from Step 2)
3. Subtract from xₙ → this gives xₙ₊₁
4. Write it down, then use xₙ₊₁ as the next input

**Keep a table — it is your best protection against errors:**

| Iteration (n) | xₙ | f(xₙ) | f(xₙ) / D | xₙ₊₁ = xₙ − f(xₙ)/D |
|---|---|---|---|---|
| 0 | x₀ (initial guess) | compute | compute | compute |
| 1 | result above | compute | compute | compute |
| 2 | ... | ... | ... | ... |

> Notice: unlike standard Newton-Raphson, you do NOT need an f'(xₙ) column — the denominator column is always just f(xₙ) divided by the same D.

---

## STEP 4 — Know When to Stop

Same three options as standard Newton-Raphson:

**Criterion 1 — Function value near zero:**
```
|f(xₙ)| < ε     (e.g. ε = 0.0001)
```

**Criterion 2 — Change between steps is tiny:**
```
|xₙ₊₁ − xₙ| < ε
```

**Criterion 3 — Fixed number of iterations:**
If the problem says "do 3 iterations," do exactly 3 and report the final xₙ.

> In exam problems, Criterion 3 is the most common instruction.

---

## STEP 5 — Report Your Answer

- State: `x ≈ [final xₙ]`
- Round to the precision asked (typically 4–6 decimal places)
- Verify: plug back into f(x) and confirm the result is close to 0

---

## STEP 6 — Watch Out for These Mistakes

| Mistake | How to Avoid It |
|---|---|
| Updating the denominator each iteration | **Never.** D is fixed at f'(x₀). Write it once and stop. |
| Using f'(xₙ) instead of f'(x₀) | The whole point of the modified method is the frozen denominator — always x₀ in the subscript |
| Wrong derivative (sign errors on trig) | Derivative of cos(x) is **−sin(x)**, not +sin(x). Double-check before freezing D. |
| Rounding x₀ derivative too early | Carry at least 4 decimal places in D; early rounding compounds across all iterations |
| Confusing which method you're using | Modified N-R denominator has x₀ subscript; standard has xₙ subscript — always check which one the problem asks for |

---

## COMPLETE WORKED SKELETON — Fill This in for Any Problem

```
Given:       f(x)  = _______________
Derivative:  f'(x) = _______________

Initial guess:  x₀ = ___

Fixed denominator (computed ONCE):
  D = f'(x₀) = f'(___) = _______________ = ___
                                              ↑ Box this number — it never changes.

--- Iteration 1 ---
f(x₀)  = _______________  =  ___
x₁ = x₀ − f(x₀) / D
   = ___ − ___ / ___
   = ___

--- Iteration 2 ---
f(x₁)  = _______________  =  ___
x₂ = x₁ − f(x₁) / D
   = ___ − ___ / ___
   = ___

--- Iteration 3 ---
f(x₂)  = _______________  =  ___
x₃ = x₂ − f(x₂) / D
   = ___ − ___ / ___
   = ___

Approximate root ≈  ___
```

---

## SIDE-BY-SIDE MENTAL MODEL

```
Standard Newton-Raphson          Modified Newton-Raphson
────────────────────────         ────────────────────────
x₁ = x₀ − f(x₀)/f'(x₀)         x₁ = x₀ − f(x₀)/f'(x₀)   ← identical first step
x₂ = x₁ − f(x₁)/f'(x₁)         x₂ = x₁ − f(x₁)/f'(x₀)   ← denominator FROZEN
x₃ = x₂ − f(x₂)/f'(x₂)         x₃ = x₂ − f(x₂)/f'(x₀)   ← denominator FROZEN
        ↑                                          ↑
  subscript updates               subscript stays 0 always
```

The first iteration is always identical for both methods. Differences only appear from iteration 2 onward.

---

## ONE-LINE MEMORY AID

```
Modified N-R  =  Standard N-R,  but the denominator never leaves x₀.
```

If your exam asks you to compare the two methods, the answer is always: **same formula, same result, frozen denominator, slightly slower but cheaper.**
