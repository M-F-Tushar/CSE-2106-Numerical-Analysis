# The Newton-Raphson Method
## Finding Roots at Rocket Speed

---

## 🧠 Why We Need Something Faster

Bisection and Regula Falsi are reliable but can be slow. Fixed Point Iteration depends heavily on how you rearrange the equation.

Newton-Raphson is the Formula 1 car of root-finding methods. It converges dramatically faster than the others — often finding the root in just 3–5 iterations, regardless of how messy the function is.

The trade-off? It needs the derivative of the function.

---

## 🔍 The Big Idea — Tangent Lines

Here's the intuition:

Imagine you're standing on a hill (the graph of f(x)), looking for where the ground is flat and crosses sea level (the root, where f(x) = 0).

Newton-Raphson says: *"Draw a straight tangent line from where you're standing, and see where that line crosses sea level. Jump to that point. Repeat."*

Each tangent line gives you a better and better guess of where the root is.

---

## 📐 Deriving the Formula

At a current guess xₙ, the tangent line to f(x) has:

- **Height:** f(xₙ)
- **Slope:** f'(xₙ) (the derivative)

The tangent line equation is:

```
y − f(xₙ) = f'(xₙ) · (x − xₙ)
```

We want where this line hits y = 0:

```
0 − f(xₙ) = f'(xₙ) · (x − xₙ)

x − xₙ = −f(xₙ) / f'(xₙ)

x = xₙ − f(xₙ) / f'(xₙ)
```

### ✅ The Newton-Raphson Formula

```
xₙ₊₁ = xₙ − f(xₙ) / f'(xₙ)
```

That's it. Beautifully simple.

---

## 📖 Story Example — f(x) = 3x − cos(x) − 1

### Scene Setup

You're a land surveyor trying to find the exact point where a winding road crosses sea level. Rather than slowly narrowing down a range, you take a laser measurement at your current position, figure out where sea level should be based on your angle, and walk there. Then you measure again. In just a few steps, you're standing exactly at sea level.

### Setup: Find the Derivative

```
f(x)  = 3x − cos(x) − 1
f'(x) = 3 + sin(x)
```

### Choose Initial Guess

Let **x₀ = 0.5**

---

### Iteration 1

```
f(0.5)  = 3(0.5) − cos(0.5) − 1
        = 1.5 − 0.8776 − 1
        = −0.3776

f'(0.5) = 3 + sin(0.5)
        = 3 + 0.4794
        = 3.4794

x₁ = 0.5 − (−0.3776) / 3.4794
   = 0.5 + 0.1085
   = 0.6085
```

One step and we're already at 0.6085 — very close to the true root 0.607!

---

### Iteration 2

```
f(0.6085)  = 3(0.6085) − cos(0.6085) − 1
           = 1.8255 − 0.8202 − 1
           = 0.0053

f'(0.6085) = 3 + sin(0.6085)
           = 3 + 0.5719
           = 3.5719

x₂ = 0.6085 − 0.0053 / 3.5719
   = 0.6085 − 0.00148
   = 0.6070
```

---

### Iteration 3

```
f(0.6070)  = 3(0.6070) − cos(0.6070) − 1
           = 1.8210 − 0.8212 − 1
           = −0.0002

f'(0.6070) = 3 + sin(0.6070)
           = 3 + 0.5702
           = 3.5702

x₃ = 0.6070 − (−0.0002) / 3.5702
   = 0.6070 + 0.000056
   = 0.6071          ← ✅ CORRECTED (original text incorrectly stated 0.6070)
```

**Converged! ✅**

---

### The Speed is Incredible

| Iteration | xₙ                  |
|-----------|---------------------|
| 0         | 0.5000 (initial guess) |
| 1         | 0.6085              |
| 2         | 0.6070              |
| 3         | 0.6071              |

Compare this to Bisection which needed 20+ iterations for the same precision!

This is called **quadratic convergence** — the number of correct decimal places roughly doubles with each step.

### ✅ Final Answer: x ≈ 0.607102

---

## 🐍 Python Code

```python
import math

# The function f(x)
def f(x):
    return 3*x - math.cos(x) - 1

# The derivative f'(x)
def df(x):
    return 3 + math.sin(x)

def newton_raphson(x0=0.5, iterations=5):
    print(f"{'Iteration':<12} {'Root Approximation'}")

    x1 = x0
    for i in range(1, iterations + 1):
        # Newton-Raphson formula
        x1 = x0 - f(x0) / df(x0)
        print(f"{i:<12} {x1:.6f}")
        x0 = x1

    print(f"\nApproximate root = {x1:.6f}")
    return x1

# Run the method
newton_raphson(x0=0.5)
```

### Output

```
Iteration    Root Approximation
1            0.608519
2            0.607102
3            0.607102
4            0.607102
5            0.607102

Approximate root = 0.607102
```

> **Notice:** It converges by iteration 2 and stays locked in. That's Newton-Raphson's power.

---

## ⚠️ When Newton-Raphson Can Fail

As powerful as it is, Newton-Raphson has failure modes:

| Problem | What Happens |
|---|---|
| f'(x) = 0 at some point | Division by zero — method crashes |
| Bad initial guess | May converge to wrong root, or diverge |
| Function has multiple roots | May jump between different roots |
| Function oscillates | May loop forever without converging |

**Rule of thumb:** Start with a guess that's reasonably close to the root, and check that f'(x) ≠ 0 in that region.

---

## 🎯 Key Takeaways

- Newton-Raphson uses the **tangent line** at each guess to zoom in on the root.
- The formula: `xₙ₊₁ = xₙ − f(xₙ) / f'(xₙ)`
- It converges **quadratically** — incredibly fast compared to other methods.
- It **requires the derivative** f'(x) — which means you need to differentiate your function.
- It **can fail** with a bad initial guess or when the derivative is zero.
- Real root for f(x) = 3x − cos(x) − 1: **x ≈ 0.607102**

---

---

# 📋 Final Revision Section — Everything You Need to Implement Newton-Raphson

> This section is your complete, self-contained implementation guide. Read this before solving any problem.

---

## STEP 0 — Understand What You Are Solving

You are given an equation like `f(x) = 0` and you need to find the value of `x` (called the **root**) where the function equals zero.

Newton-Raphson does this by starting at a guess and repeatedly improving it using the tangent line trick.

---

## STEP 1 — Write Down f(x) and Find f'(x)

Before you touch numbers, you need two things:

**1. The function itself:** This is f(x) — it is what the problem gives you.

**2. Its derivative:** This is f'(x) — you must differentiate f(x) yourself.

**Example:**
```
f(x)  = 3x − cos(x) − 1
f'(x) = 3 + sin(x)        ← derivative of (3x) is 3, derivative of (−cos x) is +sin x, derivative of (−1) is 0
```

Common derivative rules you must remember for this type of problem:

| Function term | Its derivative |
|---|---|
| constant (e.g. −1) | 0 |
| ax | a |
| xⁿ | n·xⁿ⁻¹ |
| sin(x) | cos(x) |
| cos(x) | −sin(x) |
| eˣ | eˣ |
| ln(x) | 1/x |

> ⚠️ This is the step where most mistakes happen. Double-check your derivative before proceeding.

---

## STEP 2 — Choose Your Initial Guess x₀

You need a starting point x₀. The problem will usually give this to you, or you can pick one by:

- Trying x₀ = 0, 0.5, or 1 and seeing which makes f(x₀) small
- Sketching a rough graph of f(x) and eyeballing where it crosses zero

**Rules for a safe initial guess:**
- f'(x₀) must NOT be zero (or close to zero) — if the derivative is zero at your starting point, the method crashes with division by zero
- The guess should ideally be on the same side of the root as where the function is well-behaved
- If you get a diverging sequence (values getting bigger and bigger), your guess is bad — try a different one

---

## STEP 3 — Apply the Formula Repeatedly

The one formula you must memorize:

```
xₙ₊₁ = xₙ − f(xₙ) / f'(xₙ)
```

**How to execute each iteration by hand:**

For each iteration n = 0, 1, 2, ...:

1. Plug xₙ into f(x) → compute f(xₙ)
2. Plug xₙ into f'(x) → compute f'(xₙ)
3. Divide: f(xₙ) / f'(xₙ)
4. Subtract from xₙ → this is your new xₙ₊₁
5. Write it down, then use xₙ₊₁ as the new input for the next iteration

**Keep a table as you go — it prevents errors:**

| Iteration (n) | xₙ | f(xₙ) | f'(xₙ) | xₙ₊₁ = xₙ − f/f' |
|---|---|---|---|---|
| 0 | (your guess) | compute | compute | compute |
| 1 | (result above) | compute | compute | compute |
| 2 | ... | ... | ... | ... |

---

## STEP 4 — Know When to Stop (Stopping Criteria)

You stop iterating when one of these is satisfied:

**Criterion 1 — Value of function is near zero:**
```
|f(xₙ)| < ε       (e.g. ε = 0.0001)
```
This means the current guess is close enough to the actual root.

**Criterion 2 — Change between iterations is tiny:**
```
|xₙ₊₁ − xₙ| < ε
```
This means the answer has stabilised and is no longer changing meaningfully.

**Criterion 3 — Fixed number of iterations:**
If the problem says "perform 3 iterations" or "iterate 5 times," just do exactly that many and report the final xₙ as your answer. No further check needed.

> In exam problems, Criterion 3 is the most common — you will be told how many iterations to do.

---

## STEP 5 — Report Your Answer

After the iterations are done:

- State the approximate root: `x ≈ [final xₙ value]`
- Round to the number of decimal places the problem asks for (typically 4–6)
- Verify by plugging back in: compute f(final x) and confirm it is close to 0

---

## STEP 6 — Watch Out for These Mistakes

| Mistake | How to Avoid It |
|---|---|
| Wrong derivative of f(x) | Re-derive carefully; watch signs on trig functions (derivative of cos x is **−sin x**, not +sin x) |
| Using wrong iteration value | Always use the most recent xₙ — never reuse an old value |
| Rounding too early | Carry at least 4–6 decimal places throughout; round only at the final answer |
| Skipping f'(x) = 0 check | Before starting, verify f'(x₀) ≠ 0 |
| Reporting x₂ when x₃ was asked | Count your iterations carefully — n=0 is the initial guess, n=1 is the first computed value |

---

## COMPLETE WORKED SKELETON — Fill This in for Any Problem

```
Given:     f(x) = _______________
Derivative: f'(x) = _______________

Initial guess: x₀ = ___

--- Iteration 1 ---
f(x₀)  = _______________  =  ___
f'(x₀) = _______________  =  ___
x₁ = x₀ − f(x₀)/f'(x₀)  =  ___ − ___/___  =  ___

--- Iteration 2 ---
f(x₁)  = _______________  =  ___
f'(x₁) = _______________  =  ___
x₂ = x₁ − f(x₁)/f'(x₁)  =  ___ − ___/___  =  ___

--- Iteration 3 ---
f(x₂)  = _______________  =  ___
f'(x₂) = _______________  =  ___
x₃ = x₂ − f(x₂)/f'(x₂)  =  ___ − ___/___  =  ___

Approximate root ≈  ___  (converged / within tolerance)
```

---

## ONE-LINE MEMORY AID

```
Next guess  =  Current guess  −  (function value) / (derivative value)
```

If f(xₙ) is negative and f'(xₙ) is positive → you ADD to xₙ (moving right toward root)
If f(xₙ) is positive and f'(xₙ) is positive → you SUBTRACT from xₙ (moving left toward root)

This is a quick sanity check to catch sign errors immediately.
