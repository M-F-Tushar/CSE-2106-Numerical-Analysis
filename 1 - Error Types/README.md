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
