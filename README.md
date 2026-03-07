# CSE-2106 — Numerical Analysis

> Python implementations of core numerical methods covered in the CSE-2106 course, with detailed explanations, worked examples, and iteration-by-iteration output for each algorithm.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Topics Covered](#topics-covered)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About the Project

This repository contains Python implementations of 8 fundamental numerical analysis topics as part of the **CSE-2106 Numerical Analysis** course. The goal is to bridge theory and practice — each topic has a dedicated folder with a beginner-friendly explanation, the mathematical derivation, a fully-worked example, and a corresponding Python script.

All root-finding methods (topics 2–7) use the same benchmark equation to make convergence comparison straightforward:

```
f(x) = 3x - cos(x) - 1 = 0      (known root ≈ 0.607102)
```

---

## Getting Started

### Prerequisites

- Python 3.x
- No external libraries required — only the built-in `math` module is used

### Installation

```bash
git clone https://github.com/<your-username>/CSE-2106-Numerical-Analysis.git
cd CSE-2106-Numerical-Analysis
```

---

## Usage

All scripts are in the `0 - Program Implementation/` folder. Run any script directly with Python:

```bash
python "0 - Program Implementation/2 - Bisection Method.py"
```

**Script `1 - Error Calculations.py`** prompts for interactive input:

```
Enter the true value: 3.0
Enter the approximate value: 2.0

Absolute Error   = 1.0
Relative Error   = 0.333333
Percentage Error = 33.3333%
```

**All other scripts** use hardcoded initial values and print a formatted iteration table to stdout. Example output from the Bisection Method:

```
Iteration |        a |        b |        c |     f(c)
---------------------------------------------------------
        1 | 0.000000 | 1.000000 | 0.500000 | -0.377583
        2 | 0.500000 | 1.000000 | 0.750000 |  0.681314
        ...
Approximate root: 0.607102
```

---

## Topics Covered

| # | Topic | Method Type | Folder |
|---|-------|-------------|--------|
| 1 | Error Types | Error Metrics | [1 - Error Types](./1%20-%20Error%20Types/) |
| 2 | Bisection Method | Root Finding | [2 - Bisection Method](./2%20-%20Bisection%20Method/) |
| 3 | Regula Falsi Method | Root Finding | [3 - Regula Falsi Method](./3%20-%20Regula%20Falsi%20Method/) |
| 4 | Fixed Point Iteration | Root Finding | [4 - Fixed Point Iteration Method](./4%20-%20Fixed%20Point%20Iteration%20Method/) |
| 5 | Newton-Raphson Method | Root Finding | [5 - Newton-Raphson Method](./5%20-%20Newton-Raphson%20Method/) |
| 6 | Modified Newton-Raphson | Root Finding | [6 - Modified Newton-Raphson Method](./6%20-%20Modified%20Newton-Raphson%20Method/) |
| 7 | Secant Method | Root Finding | [7 - Secant Method](./7%20-%20Secant%20Method/) |
| 8 | Jacobi Method | Linear System Solver | [8 - Jacobi Method](./8%20-%20Jacobi%20Method/) |

### Root-Finding Method Comparison

| Method | Derivative Needed | Initial Input | Convergence |
|--------|:-----------------:|---------------|:-----------:|
| Bisection | No | Bracket `[a, b]` | Linear |
| Regula Falsi | No | Bracket `[a, b]` | Superlinear |
| Fixed Point Iteration | No | Single guess `x0` | Linear |
| Newton-Raphson | Yes (every step) | Single guess `x0` | Quadratic |
| Modified Newton-Raphson | Yes (once) | Single guess `x0` | Linear |
| Secant Method | No | Two guesses `x0, x1` | Superlinear (~1.618) |

---

## Repository Structure

```
CSE-2106-Numerical-Analysis/
│
├── README.md
│
├── 0 - Program Implementation/     # Python scripts for all 8 topics
│   ├── 1 - Error Calculations.py
│   ├── 2 - Bisection Method.py
│   ├── 3 - Regula Falsi Method.py
│   ├── 4 - Fixed Point Iteration.py
│   ├── 5 - Newton Raphson.py
│   ├── 6 - Modified Newton Raphson.py
│   ├── 7 - Secant Method.py
│   └── 8 - Jacobi Method.py
│
├── 1 - Error Types/README.md
├── 2 - Bisection Method/README.md
├── 3 - Regula Falsi Method/README.md
├── 4 - Fixed Point Iteration Method/README.md
├── 5 - Newton-Raphson Method/README.md
├── 6 - Modified Newton-Raphson Method/README.md
├── 7 - Secant Method/README.md
└── 8 - Jacobi Method/README.md
```

Each numbered folder contains a `README.md` covering:
- Conceptual explanation with real-world analogies
- Mathematical derivation of the formula
- Step-by-step worked example with iteration tables
- Annotated Python code
- Expected sample output
- Pros, cons, and known failure conditions

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-topic`)
3. Commit your changes (`git commit -m 'Add: your topic'`)
4. Push to the branch (`git push origin feature/your-topic`)
5. Open a Pull Request

Please follow the existing folder structure and include both a Python script in `0 - Program Implementation/` and a `README.md` in a new topic folder.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact

If you have questions or suggestions, feel free to open an [issue](https://github.com/<your-username>/CSE-2106-Numerical-Analysis/issues).
