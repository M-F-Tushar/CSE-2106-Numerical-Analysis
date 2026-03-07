# The Newton-Raphson Method
## Finding Roots at Rocket Speed

---

## 🧠 Why We Need Something Faster

Bisection and Regula Falsi are reliable but can be slow. Fixed Point Iteration depends heavily on how you rearrange the equation.

Newton-Raphson is the **Formula 1 car** of root-finding methods. It converges dramatically faster than the others — often finding the root in just 3–5 iterations, regardless of how messy the function is.

The trade-off? It needs the **derivative** of the function.

---

## 🔍 The Big Idea — Tangent Lines

Here's the intuition:

Imagine you're standing on a hill (the graph of `f(x)`), looking for where the ground is flat and crosses sea level (the root, where `f(x) = 0`).

Newton-Raphson says: *"Draw a straight tangent line from where you're standing, and see where that line crosses sea level. Jump to that point. Repeat."*

Each tangent line gives you a better and better guess of where the root is.

---

## 📐 Deriving the Formula

At a current guess `xₙ`, the tangent line to `f(x)` has:
- Height: `f(xₙ)`
- Slope: `f'(xₙ)` (the derivative)

The tangent line equation is:
```
y − f(xₙ) = f'(xₙ) · (x − xₙ)
```

We want where this line hits `y = 0`:
```
0 − f(xₙ) = f'(xₙ) · (x − xₙ)

x − xₙ = −f(xₙ) / f'(xₙ)

x = xₙ − f(xₙ) / f'(xₙ)
```

### The Newton-Raphson Formula

```
xₙ₊₁ = xₙ − f(xₙ) / f'(xₙ)
```

That's it. Beautifully simple.

---

## 📖 Story Example — `f(x) = 3x − cos(x) − 1`

### Scene Setup

You're a land surveyor trying to find the exact point where a winding road crosses sea level. Rather than slowly narrowing down a range, you take a **laser measurement** at your current position, figure out where sea level *should* be based on your angle, and walk there. Then you measure again. In just a few steps, you're standing exactly at sea level.

### Setup: Find the Derivative

```
f(x) = 3x − cos(x) − 1

f'(x) = 3 + sin(x)
```

### Choose Initial Guess

Let `x₀ = 0.5`

---

### Iteration 1

```
f(0.5) = 3(0.5) − cos(0.5) − 1
       = 1.5 − 0.8776 − 1
       = −0.3776

f'(0.5) = 3 + sin(0.5)
        = 3 + 0.4794
        = 3.4794

x₁ = 0.5 − (−0.3776) / 3.4794
   = 0.5 + 0.1085
   = 0.6085
```

One step and we're already at **0.6085** — very close to the true root 0.607!

---

### Iteration 2

```
f(0.6085) = 3(0.6085) − cos(0.6085) − 1
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
x₃ ≈ 0.6070  (f(0.6070) ≈ 0)
```

**Converged!** ✅

---

### The Speed is Incredible

| Iteration | xₙ |
|---|---|
| 0 | 0.5000 (initial guess) |
| 1 | 0.6085 |
| 2 | 0.6070 |
| 3 | 0.6071 |

Compare this to Bisection which needed **20+ iterations** for the same precision!

This is called **quadratic convergence** — the number of correct decimal places roughly *doubles* with each step.

### ✅ Final Answer: `x ≈ 0.607102`

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

Notice: it **converges by iteration 2** and stays locked in. That's Newton-Raphson's power.

---

## ⚠️ When Newton-Raphson Can Fail

As powerful as it is, Newton-Raphson has failure modes:

| Problem | What Happens |
|---|---|
| `f'(x) = 0` at some point | Division by zero — method crashes |
| Bad initial guess | May converge to wrong root, or diverge |
| Function has multiple roots | May jump between different roots |
| Function oscillates | May loop forever without converging |

**Rule of thumb:** Start with a guess that's reasonably close to the root, and check that `f'(x) ≠ 0` in that region.

---

## 🎯 Key Takeaways

- Newton-Raphson uses the **tangent line** at each guess to zoom in on the root.
- The formula: `xₙ₊₁ = xₙ − f(xₙ) / f'(xₙ)`
- It converges **quadratically** — incredibly fast compared to other methods.
- It **requires the derivative** `f'(x)` — which means you need to differentiate your function.
- It can fail with a bad initial guess or when the derivative is zero.
- Real root for `f(x) = 3x − cos(x) − 1`: **x ≈ 0.607102**
