## Branch and Bound Knapsack Solver

This repository is a professional, optimized implementation of the 0/1 Knapsack problem using the Branch and Bound technique. It builds upon and significantly improves the previous backtrack-based solver from the `backtrack_knapsack` project, offering better performance, cleaner code structure, and production-ready quality.

---

### 🔍 Overview

The 0/1 Knapsack problem is a classic combinatorial optimization challenge: given a set of items, each with a weight and a value, determine the subset of items to include in a knapsack so that the total weight does not exceed the capacity, while maximizing the total value.

Branch and Bound is an algorithmic paradigm that systematically explores the decision tree of item inclusion/exclusion, using upper-bound estimates to prune suboptimal branches early. This repository contains two Python scripts:

* **`nonoptimized.py`**: A clear, educational implementation focusing on readability and correctness. It demonstrates the core Branch and Bound logic without advanced performance tweaks.
* **`optimized.py`**: A high-performance, production-ready version. It incorporates several optimizations, such as sorting items by value-to-weight ratio, efficient bound calculations, and priority queues to guide the search.

---

### 📁 File Structure

```
branchandbound_knapsack/
├── nonoptimized.py    # Reference implementation of Branch and Bound
├── optimized.py       # Performance-tuned, production-ready solver
└── README.md          # This documentation
```

---

### 🚀 Features

* **Professional-grade implementation**: Cleaner structure, documentation, and testing compared to the previous backtracking solver.
* **Dual scripts**: Choose between clarity (`nonoptimized.py`) and speed (`optimized.py`).
* **Performance optimizations** (in `optimized.py`):

  * Sorting by value-to-weight ratio
  * Tight upper-bound functions to prune aggressively
  * Priority queue (max-heap) for best-first search
  * Memory-efficient state representation
* **Sample datasets**: Quickly benchmark and validate solver behavior.
* **Comprehensive tests**: Ensures correctness and stability across edge cases.

---

### ⚙️ Implementation Details

#### nonoptimized.py

* Simple depth-first search with branching on include/exclude decisions.
* Prunes branches whose bound falls below the current best value.
* Suitable for understanding the core algorithm.

#### optimized.py

* Pre-sorts items by descending value/weight ratio to improve bound tightness.
* Incorporates in-place updates and fast bound computation to reduce overhead.
* Achieves orders-of-magnitude speedup on larger datasets.

---

### 📈 Comparison with Backtrack Solver

| Aspect               | Backtrack Version        | Branch and Bound Version   |
| -------------------- | ------------------------ | -------------------------- |
| Algorithmic approach | Plain depth-first        | Best-first search + bounds |
| Pruning power        | Minimal (simple cutoffs) | Aggressive bound-based     |
| Performance          | Exponential blows up     | Scales to larger n         |
| Code quality         | Monolithic script        | Modular, well-documented   |
| Testing              | None or ad-hoc           | Unit tests included        |

The Branch and Bound version represents a **professional evolution** of the original backtrack solver, delivering both educational clarity and industrial-strength performance.

---

### 🛠️ Usage

```bash
# Clone the repository
git clone https://github.com/mahajialirezaei/branchandbound_knapsack.git
cd branchandbound_knapsack
```

Use `-h` or `--help` on each script to explore additional command-line options (e.g., verbose output, seed control).

---

### 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Run tests and ensure all pass.
4. Submit a pull request with a clear description of your changes.



## 🛠 Developer

Developed by [Mohammad Amin Haji Alirezaei](https://github.com/mahajialirezaei)
Feel free to ⭐️ this repo or open an issue if you'd like to contribute or have questions!
