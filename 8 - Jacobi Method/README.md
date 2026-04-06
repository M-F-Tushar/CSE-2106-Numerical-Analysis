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

---

---

## 📋 Final Revision Section — Everything You Need to Implement the Jacobi Method

This section is your complete, step-by-step implementation guide. Read this alone and you will know exactly what to do.

---

### STEP 0 — Understand What Kind of Problem This Is

The Jacobi Method solves a **system of linear equations** — multiple equations with multiple unknowns. It is not for finding roots of a single equation.

You are looking for values of `x`, `y`, `z` (or more unknowns) that **satisfy all equations simultaneously**.

The method works by **guessing all unknowns, then repeatedly refining those guesses** until they stop changing — i.e., they have converged to the true solution.

---

### STEP 1 — Write Down Your System and Check It

Make sure your system has the same number of equations as unknowns. Write it clearly.

**Example:**
```
10x +  y +  z = 12
 2x + 10y +  z = 13
 2x +  2y + 10z = 14
```

Three equations, three unknowns — good.

---

### STEP 2 — Check for Diagonal Dominance BEFORE You Start

This is the most important pre-check. For each row, ask:

> Is the absolute value of the diagonal coefficient **strictly greater than** the sum of absolute values of all other coefficients in the same row?

**Formula for each row i:**
```
|aᵢᵢ| > Σ |aᵢⱼ|   (for all j ≠ i)
```

**Example check:**
```
Row 1: |10| > |1| + |1|  →  10 > 2  ✅
Row 2: |10| > |2| + |1|  →  10 > 3  ✅
Row 3: |10| > |2| + |2|  →  10 > 4  ✅
```

**If all rows pass:** Jacobi is guaranteed to converge. Proceed.

**If any row fails:** Try rearranging the rows so that the largest coefficient in each equation ends up on the diagonal. If you cannot make it diagonally dominant, Jacobi may diverge — consider a different method.

---

### STEP 3 — Rearrange Each Equation to Isolate One Variable

From each equation, solve for its diagonal variable (move everything else to the right side and divide by the diagonal coefficient).

**Pattern:**
```
aᵢᵢ · xᵢ = bᵢ − (sum of all other terms)
xᵢ = (bᵢ − sum of other terms) / aᵢᵢ
```

**Example:**
```
Equation 1 isolates x:  x = (12 −  y −  z) / 10
Equation 2 isolates y:  y = (13 − 2x −  z) / 10
Equation 3 isolates z:  z = (14 − 2x − 2y) / 10
```

These three formulas are what you will apply every iteration.

---

### STEP 4 — Set Your Initial Guess

Start all unknowns at zero unless you have a better estimate:
```
x = 0,   y = 0,   z = 0
```

This always works for diagonally dominant systems.

---

### STEP 5 — Apply One Iteration (The Core Rule)

This is the most critical step, and the one most people get wrong.

**THE RULE: Compute ALL new values using ONLY the OLD values. Then replace ALL old values at once.**

```
x_new = (12 −  y_old −  z_old) / 10
y_new = (13 − 2·x_old −  z_old) / 10
z_new = (14 − 2·x_old − 2·y_old) / 10

← Only after all three are computed:
x_old ← x_new
y_old ← y_new
z_old ← z_new
```

Do **not** use `x_new` when computing `y_new` in the same iteration. That would make it Gauss-Seidel, not Jacobi.

---

### STEP 6 — Work Through the First Two Iterations by Hand

Practice is essential. If you can do two iterations cleanly, you understand the method.

**Iteration 1** (starting from x=0, y=0, z=0):
```
x₁ = (12 − 0 − 0) / 10 = 1.2
y₁ = (13 − 0 − 0) / 10 = 1.3
z₁ = (14 − 0 − 0) / 10 = 1.4
```

**Iteration 2** (using x=1.2, y=1.3, z=1.4 — all from previous step):
```
x₂ = (12 − 1.3 − 1.4) / 10 = 9.3  / 10 = 0.93
y₂ = (13 − 2.4 − 1.4) / 10 = 9.2  / 10 = 0.92
z₂ = (14 − 2.4 − 2.6) / 10 = 9.0  / 10 = 0.90
```

Notice the oscillation: first you overshoot (1.2, 1.3, 1.4), then undershoot (0.93, 0.92, 0.90). This is normal. The values close in on the true answer with each iteration.

---

### STEP 7 — Know When to Stop (Stopping Criteria)

Stop iterating when one of these is met:

| Condition | What it means |
|---|---|
| `max(|x_new − x_old|, |y_new − y_old|, |z_new − z_old|) < tolerance` | All variables barely changed |
| Substitute back and verify `Ax = b` is satisfied | Direct accuracy check |
| Maximum iterations reached | Safety cap |

**Typical tolerance:** `1e-6` for textbook problems.

For this example, the solution stabilizes to `x = y = z = 1.0` around **iteration 11**.

---

### STEP 8 — Write the Code (Python Template)

```python
def jacobi_method(x0=0.0, y0=0.0, z0=0.0, tol=1e-6, max_iter=100):
    x, y, z = x0, y0, z0

    print(f"{'Iter':<8} {'x':<12} {'y':<12} {'z':<12}")

    for i in range(1, max_iter + 1):
        # Compute ALL new values using OLD values only — do not mix!
        x_new = (12 -  y -  z) / 10   # ← Replace with your own equations
        y_new = (13 - 2*x -  z) / 10
        z_new = (14 - 2*x - 2*y) / 10

        print(f"{i:<8} {x_new:<12.6f} {y_new:<12.6f} {z_new:<12.6f}")

        # Check stopping condition — largest change among all variables
        if max(abs(x_new - x), abs(y_new - y), abs(z_new - z)) < tol:
            print(f"\nConverged at iteration {i}!")
            print(f"x = {x_new:.6f}, y = {y_new:.6f}, z = {z_new:.6f}")
            return x_new, y_new, z_new

        # Update ALL at once — this is the defining rule of Jacobi
        x, y, z = x_new, y_new, z_new

    print("Did not converge within max iterations.")
    return x, y, z

jacobi_method()
```

---

### STEP 9 — Verify Your Answer

Always substitute your final values back into the **original** equations and confirm all three hold.

**Example verification for x=1, y=1, z=1:**
```
10(1) +  1 +  1 = 12  ✅
 2(1) + 10(1) + 1 = 13  ✅
 2(1) +  2(1) + 10(1) = 14  ✅
```

If any equation fails, either the method did not converge fully (run more iterations) or there was an error in your rearrangement step.

---

### STEP 10 — Common Mistakes to Avoid

| Mistake | Why it's wrong | Fix |
|---|---|---|
| Using updated `x_new` when computing `y_new` in same iteration | That is Gauss-Seidel, not Jacobi | Compute all three new values first, then assign |
| Not checking diagonal dominance | Method may diverge silently | Always check before starting |
| Failing to rearrange equations correctly | Wrong isolated formula = wrong answer | Double-check by substituting back |
| Starting with a very bad initial guess | May slow convergence or diverge | Start at all zeros, or near the expected solution |
| Using `=` to update in-place in code | Python line order matters; updating `x` before using it in `y` formula breaks Jacobi | Use temporary variables `x_new, y_new, z_new` |

---

### STEP 11 — Quick Mental Checklist Before You Submit / Run

```
✅ Same number of equations and unknowns?
✅ Checked diagonal dominance for every row?
✅ Rearranged each equation correctly to isolate its variable?
✅ Started from initial guess (all zeros is fine)?
✅ Computed ALL new values using ONLY old values in each iteration?
✅ Updated ALL variables simultaneously AFTER computing all new values?
✅ Set a stopping condition (tolerance or max iterations)?
✅ Verified the final answer by substituting back into original equations?
```

---

### Summary in One Line

> **Rearrange each equation to isolate one variable → start at zero → each iteration, compute all new values from the old ones simultaneously → replace old with new → repeat until values stop changing.**
