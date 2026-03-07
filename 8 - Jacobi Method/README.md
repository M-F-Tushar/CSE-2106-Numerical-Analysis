# The Jacobi Method
## Solving Systems of Linear Equations by Iteration

---

## 🧠 A New Kind of Problem

All the methods we've covered so far (Bisection, Newton-Raphson, etc.) solve for **one root of one equation**.

The Jacobi Method is different. It solves a **system of multiple equations with multiple unknowns** — all at the same time.

For example:
```
10x + y + z  = 12
2x + 10y + z = 13
2x + 2y + 10z = 14
```

Three equations, three unknowns (`x`, `y`, `z`). We need to find all three values simultaneously.

---

## 🔍 The Key Insight

You *could* solve this system using algebra (substitution, elimination, matrices). But for **large systems** (think: 1000 equations with 1000 unknowns), those algebraic methods become extremely slow.

The Jacobi Method offers an alternative:

> **Start with a guess for all unknowns. Then repeatedly update each variable using the other variables' current values — until everything stabilizes.**

---

## 🔄 The Algorithm

### Step 1: Rearrange each equation to isolate one variable

From the system:
```
10x + y + z  = 12   →   x = (12 − y − z) / 10
2x + 10y + z = 13   →   y = (13 − 2x − z) / 10
2x + 2y + 10z = 14  →   z = (14 − 2x − 2y) / 10
```

### Step 2: Start with an initial guess

```
x₀ = 0,   y₀ = 0,   z₀ = 0
```

(All zeros is the classic starting point.)

### Step 3: Plug the old values into the right-hand side to get new values

```
x_new = (12 − y_old − z_old) / 10
y_new = (13 − 2·x_old − z_old) / 10
z_new = (14 − 2·x_old − 2·y_old) / 10
```

### Step 4: Replace old values with new, repeat

---

## 📖 Story Example

### Scene Setup

Imagine three friends — Alex, Ben, and Chris — each need to figure out their fair share of expenses. Each person's fair share depends on what the other two paid. They each calculate their own share based on yesterday's estimates, then share their new answers. They keep doing this until everyone agrees.

That's Jacobi: **everyone updates simultaneously based on the previous round's information.**

### The System

```
10x + y + z  = 12
2x + 10y + z = 13
2x + 2y + 10z = 14
```

Isolated form:
```
x = (12 − y − z) / 10
y = (13 − 2x − z) / 10
z = (14 − 2x − 2y) / 10
```

Initial guess: `x = 0, y = 0, z = 0`

---

### Iteration 1 — Using `x₀=0, y₀=0, z₀=0`

```
x₁ = (12 − 0 − 0) / 10 = 12/10 = 1.2
y₁ = (13 − 0 − 0) / 10 = 13/10 = 1.3
z₁ = (14 − 0 − 0) / 10 = 14/10 = 1.4
```

First update: `(1.2, 1.3, 1.4)`

---

### Iteration 2 — Using `x₁=1.2, y₁=1.3, z₁=1.4`

```
x₂ = (12 − 1.3 − 1.4) / 10
   = 9.3 / 10
   = 0.93

y₂ = (13 − 2(1.2) − 1.4) / 10
   = (13 − 2.4 − 1.4) / 10
   = 9.2 / 10
   = 0.92

z₂ = (14 − 2(1.2) − 2(1.3)) / 10
   = (14 − 2.4 − 2.6) / 10
   = 9 / 10
   = 0.9
```

Second update: `(0.93, 0.92, 0.9)` — we overshot a bit, now undershooting.

---

### Iteration 3 — Using `x₂=0.93, y₂=0.92, z₂=0.9`

```
x₃ = (12 − 0.92 − 0.9) / 10
   = 10.18 / 10
   = 1.018

y₃ = (13 − 2(0.93) − 0.9) / 10
   = (13 − 1.86 − 0.9) / 10
   = 10.24 / 10
   = 1.024

z₃ = (14 − 2(0.93) − 2(0.92)) / 10
   = (14 − 1.86 − 1.84) / 10
   = 10.3 / 10
   = 1.03
```

Third update: `(1.018, 1.024, 1.03)` — converging toward 1.

---

### Full Convergence Table

| Iteration | x | y | z |
|---|---|---|---|
| 1 | 1.2 | 1.3 | 1.4 |
| 2 | 0.93 | 0.92 | 0.9 |
| 3 | 1.018 | 1.024 | 1.03 |
| 4 | 0.9946 | 0.9934 | 0.9916 |
| 5 | 1.0015 | 1.00192 | 1.0024 |
| 6 | 0.9996 | 0.9995 | 0.9993 |
| 7 | 1.00012 | 1.00015 | 1.00019 |
| ... | ... | ... | ... |
| 11 | **1.0** | **1.0** | **1.0** |

### ✅ Final Answer: `x = 1, y = 1, z = 1`

Let's verify:
```
10(1) + 1 + 1 = 12  ✅
2(1) + 10(1) + 1 = 13  ✅
2(1) + 2(1) + 10(1) = 14  ✅
```

---

## 🐍 Python Code

```python
def jacobi_method(iterations=15):
    x, y, z = 0.0, 0.0, 0.0   # Initial guesses (all zero)

    print(f"{'Iteration':<12} {'x':<10} {'y':<10} {'z':<10}")

    for i in range(1, iterations + 1):
        # Compute ALL new values using OLD values simultaneously
        x1 = (12 - y - z) / 10
        y1 = (13 - 2*x - z) / 10
        z1 = (14 - 2*x - 2*y) / 10

        print(f"{i:<12} {x1:<10.6f} {y1:<10.6f} {z1:<10.6f}")

        # Update ALL at once (this is key to Jacobi!)
        x, y, z = x1, y1, z1

    print(f"\nFinal Answer:  x = {x:.4f},  y = {y:.4f},  z = {z:.4f}")

# Run the method
jacobi_method()
```

---

## 🔑 The Critical Difference: Jacobi vs Gauss-Seidel

A common confusion is between **Jacobi** and **Gauss-Seidel** methods. Here's the key:

- **Jacobi:** All variables update using **old values only**. You compute all new values first, then replace all old values at once.
- **Gauss-Seidel:** Each variable immediately uses the **newly updated** values of previous variables.

In Python, Jacobi stores `x1, y1, z1` separately before assigning:
```python
x1 = (12 - y - z) / 10    # uses OLD y and z
y1 = (13 - 2*x - z) / 10  # uses OLD x and z
z1 = (14 - 2*x - 2*y) / 10 # uses OLD x and y
# THEN update all at once
x, y, z = x1, y1, z1
```

If you had updated `x` first and immediately used it in the `y` formula, that would be Gauss-Seidel:
```python
x = (12 - y - z) / 10       # x updated first
y = (13 - 2*x - z) / 10     # uses NEW x already!  ← Gauss-Seidel
z = (14 - 2*x - 2*y) / 10   # uses NEW x and y
```

---

## ⚠️ When Does Jacobi Work? — Diagonal Dominance

Jacobi doesn't always converge. The key condition is **diagonal dominance**:

> The coefficient on the diagonal (the main variable in each equation) must be **larger in magnitude** than the sum of all other coefficients in that row.

For our system:
```
Row 1: |10| > |1| + |1| = 2   ✅  (10 > 2)
Row 2: |10| > |2| + |1| = 3   ✅  (10 > 3)
Row 3: |10| > |2| + |2| = 4   ✅  (10 > 4)
```

All rows are diagonally dominant — Jacobi is guaranteed to converge.

If a system is **not** diagonally dominant, you may need to rearrange the equations or use a different method.

---

## 🎯 Key Takeaways

- Jacobi solves **systems of linear equations** by iteration — not single-variable root finding.
- You rearrange each equation to solve for one variable in terms of the others.
- Start with an initial guess (usually all zeros), then keep updating until values stabilize.
- **All variables update simultaneously** using the previous iteration's values — this is what makes it Jacobi (not Gauss-Seidel).
- Works best when the system is **diagonally dominant**.
- Final answer for the example: **x = 1, y = 1, z = 1**
