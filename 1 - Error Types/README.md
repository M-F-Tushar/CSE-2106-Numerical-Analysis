# Understanding Errors in Numerical Analysis
## Absolute Error, Relative Error & Percentage Error

---

## 🧠 Why Do We Even Talk About "Error"?

Imagine you're a baker. Your recipe says a cake needs exactly **3 cups of flour**. But you accidentally pour **2 cups**. Did you mess up badly? Or just a little?

That question — *"how bad is the mistake?"* — is exactly what **error measurement** is about in Numerical Analysis.

Computers and calculators can't always store or compute the *perfect* value of a number (like π or √2). They use *approximations*. Error tells us **how far off** that approximation is from the truth.

There are three ways to measure this, each answering a slightly different question.

---

## 1. 📏 Absolute Error — "How far off are you?"

### The Idea

Absolute Error simply measures the **raw gap** between the true value and your approximate value. It doesn't care about *how big* the true value is — just how big the gap is.

### Formula

```
Absolute Error = | True Value − Approximate Value |
```

> The `| |` symbols mean *absolute value* — we always make the result positive, because error is always a distance (you can't have a "negative" distance).

### Story Example

You're trying to guess the weight of a watermelon. The real weight is **3.0 kg**. You guess **2.0 kg**.

```
Absolute Error = |3.0 − 2.0| = |1.0| = 1.0 kg
```

You were off by **1 kg**. Simple and clear.

---

## 2. 🔍 Relative Error — "How bad is it *compared to* the real thing?"

### The Idea

Here's a problem with Absolute Error: **1 kg off on a 3 kg watermelon** sounds bad. But what about **1 kg off on a 1000 kg elephant**? That's barely anything!

Relative Error fixes this by comparing the absolute error **to the size of the true value**. It gives you a sense of *proportion*.

### Formula

```
Relative Error = | True Value − Approximate Value | / | True Value |
```

Or more simply:

```
Relative Error = Absolute Error / | True Value |
```

### Story Example (continued)

Same watermelon. True = 3.0 kg, Approximate = 2.0 kg.

```
Absolute Error = 1.0

Relative Error = 1.0 / 3.0 = 0.3333
```

This means your guess was off by about **33% of the true value** — which is actually quite a big mistake.

Now imagine if the true value was **1000 kg** and your absolute error was still 1.0:

```
Relative Error = 1.0 / 1000 = 0.001
```

Only 0.1% off — barely a scratch. **Same absolute error, very different relative error.**

---

## 3. 📊 Percentage Error — "Say it in percent!"

### The Idea

Percentage Error is just Relative Error dressed up in a more human-friendly outfit. People understand "33%" better than "0.3333". So we multiply Relative Error by 100.

### Formula

```
Percentage Error = (Absolute Error / |True Value|) × 100%
```

### Story Example (final piece)

```
Percentage Error = 0.3333 × 100 = 33.33%
```

Your watermelon guess was **33.33% wrong**. Your mum would not be impressed.

---

## 🔁 All Three Together — Quick Summary

| Error Type | Formula | What It Tells You |
|---|---|---|
| Absolute Error | \|True − Approx\| | Raw gap between truth and guess |
| Relative Error | Absolute Error ÷ \|True\| | Gap as a fraction of the truth |
| Percentage Error | Relative Error × 100 | Gap expressed as a percentage |

---

## 🐍 Python Code

```python
# Error Calculations: Absolute, Relative, Percentage

true_value = float(input("Enter true value: "))
approx_value = float(input("Enter approximate value: "))

# Step 1: Absolute Error
absolute_error = abs(true_value - approx_value)

# Step 2: Relative Error
relative_error = absolute_error / abs(true_value)

# Step 3: Percentage Error
percentage_error = relative_error * 100

print(f"\nAbsolute Error   = {absolute_error}")
print(f"Relative Error   = {relative_error:.6f}")
print(f"Percentage Error = {percentage_error:.4f}%")
```

### Sample Run

```
Enter true value: 3.0
Enter approximate value: 2.0

Absolute Error   = 1.0
Relative Error   = 0.333333
Percentage Error = 33.3333%
```

---

## 🎯 Key Takeaways

- Use **Absolute Error** when you need to know the plain size of the mistake.
- Use **Relative Error** when you need to compare mistakes across different scales.
- Use **Percentage Error** when you want the result to be intuitive and easy to communicate.

> In Numerical Analysis, we often want errors to be as small as possible — usually below a *tolerance* like `1e-6` (0.000001). If your error is smaller than the tolerance, your answer is "good enough."

---

## 📌 Final Revision — Everything You Need to Remember

*A complete, step-by-step mental checklist. Read this before attempting any error calculation problem.*

---

### Phase 0 — Understand the Core Idea

**Why errors exist:**
In Numerical Analysis, we rarely work with perfectly exact values. Computers approximate numbers like π, √2, or the output of iterative methods (like Bisection or Regula Falsi). Error measurement tells us **how trustworthy** an approximation is.

**Two pieces you always need:**
- The **True Value** — the exact, correct answer
- The **Approximate Value** — your computed or estimated answer

Without both, you cannot calculate any form of error.

---

### Phase 1 — Absolute Error

**Formula:**
```
Absolute Error = | True Value − Approximate Value |
```

**What it means:** The plain, raw size of the gap between your answer and the correct one. Units stay the same as the original quantity (kg, meters, seconds, etc.).

**When to use it:** When you want to know the magnitude of the mistake in concrete terms, without any comparison to scale.

**Example:**
```
True = 3.0,   Approximate = 2.0
Absolute Error = |3.0 − 2.0| = 1.0
```

**Key rule:** Always take the absolute value — the result must be ≥ 0. A negative error has no physical meaning.

> ⚠️ **Limitation:** Absolute Error alone can be misleading. An error of `1.0` means something very different when the true value is `3` versus when it is `1,000,000`.

---

### Phase 2 — Relative Error

**Formula:**
```
Relative Error = Absolute Error / | True Value |
```

**What it means:** The error expressed as a *fraction* of the true value. Answers the question: "Relative to how big the actual thing is, how bad was the mistake?"

**When to use it:** When comparing errors across different problems or scales — e.g., comparing the accuracy of two different methods, or two different quantities.

**Example:**
```
True = 3.0,   Absolute Error = 1.0
Relative Error = 1.0 / 3.0 = 0.3333

True = 1000.0,   Absolute Error = 1.0
Relative Error = 1.0 / 1000.0 = 0.001
```

Same absolute error — but `0.3333` (33% off) vs `0.001` (0.1% off) tells a very different story.

**Result is unitless** — it's a pure ratio (e.g., 0.3333, not 0.3333 kg).

> ⚠️ **Important:** The denominator is always `|True Value|`, not the approximate value. Never divide by your guess.

---

### Phase 3 — Percentage Error

**Formula:**
```
Percentage Error = Relative Error × 100
               = (Absolute Error / |True Value|) × 100%
```

**What it means:** Relative Error scaled to a percentage. Easier for humans to read and communicate — most people understand "33%" much more intuitively than "0.3333".

**Example:**
```
Relative Error = 0.3333
Percentage Error = 0.3333 × 100 = 33.33%
```

**When to use it:** Whenever you need to present or communicate an error result clearly — in reports, tables, lab work, or problem sets.

---

### Phase 4 — Step-by-Step Procedure for Any Problem

Given a **True Value** and an **Approximate Value**, always compute in this order:

**Step 1:** Compute Absolute Error
```
E_abs = |True − Approx|
```

**Step 2:** Compute Relative Error
```
E_rel = E_abs / |True|
```

**Step 3:** Compute Percentage Error
```
E_pct = E_rel × 100
```

**Step 4 (optional):** Compare to a tolerance
```
If E_abs < 1e-6  →  "Acceptable accuracy"
If E_rel < 0.01  →  "Less than 1% relative error — good"
```

---

### Phase 5 — The Three Errors Side by Side

| | Absolute Error | Relative Error | Percentage Error |
|---|---|---|---|
| Formula | `\|True − Approx\|` | `Abs / \|True\|` | `Rel × 100` |
| Units | Same as original | Unitless (ratio) | % (unitless) |
| Answers | "How big is the gap?" | "Gap as fraction of truth?" | "Gap as a percentage?" |
| Best for | Knowing raw magnitude | Comparing across scales | Communicating clearly |
| Weakness | Misleading for large values | Less intuitive | Same as relative |

---

### Phase 6 — Worked Example at a Glance

**True = 3.0 kg,   Approximate = 2.0 kg**

```
Step 1:  Absolute Error   = |3.0 − 2.0| = 1.0 kg

Step 2:  Relative Error   = 1.0 / 3.0   = 0.3333

Step 3:  Percentage Error = 0.3333 × 100 = 33.33%
```

**Interpretation:** Your approximation is off by 1 kg, which is 33.33% of the true value. This is a large error — typically unacceptable in numerical work.

---

### Phase 7 — Common Mistakes to Avoid

1. **Forgetting the absolute value.** `|True − Approx|` must be non-negative. If your computed error is negative, you forgot the absolute value.

2. **Dividing by the approximate value instead of the true value.** Relative Error always uses `|True Value|` in the denominator. Dividing by the approximation gives a different (and incorrect) measure.

3. **Confusing Relative and Percentage Error.** Relative Error is a decimal (e.g., `0.3333`). Percentage Error is `× 100` of that (e.g., `33.33%`). They carry the same information, just expressed differently.

4. **Applying Absolute Error across different scales.** If you're comparing two methods and one has `true = 5` while another has `true = 5000`, absolute errors are not directly comparable. Use relative or percentage error instead.

5. **Using the wrong "true" value.** In iterative methods (Bisection, Regula Falsi, etc.), the "true" value is the exact root — not a previous iteration. Make sure you know which value is the ground truth before computing error.

---

### Phase 8 — One-Page Quick Reference

```
Given:  True Value (T)   and   Approximate Value (A)

1. Absolute Error
   E_abs = |T − A|

2. Relative Error
   E_rel = E_abs / |T|

3. Percentage Error
   E_pct = E_rel × 100

Example:  T = 3.0,  A = 2.0
   E_abs = |3.0 − 2.0|  = 1.0
   E_rel = 1.0 / 3.0    = 0.3333
   E_pct = 0.3333 × 100 = 33.33%

Rule of thumb:
   E_rel < 0.01   →  less than 1% error  (usually acceptable)
   E_abs < 1e-6   →  within typical numerical tolerance
```

---

> Errors are not failures — they are measurements. In Numerical Analysis, no iterative method gives you a perfect answer. What matters is whether the error is *small enough* for your purpose. Always define your tolerance before you start, and stop when your error falls below it.
