# Stage 0 — Foundations

This stage exists to **set rules, structure, and discipline** before any algorithmic work begins. If Stage 0 is weak, everything after it will be sloppy. Do not rush this.

---

## 1. Objective of Stage 0

Stage 0 is about **preparation**, not problem-solving.

You are establishing:

* A strict repository structure
* Coding and documentation standards
* Mathematical prerequisites
* Banned shortcuts and bad habits
* How future stages will be evaluated

**No algorithms are implemented in this stage.**

---

## 2. Repository Structure (Mandatory)

```
stage-0/
│
├── README.md              # This file (rules, philosophy, setup)
│
├── base/
│   ├── __init__.py
│   ├── algo_base.py       # Abstract base class for all algorithms
│   ├── test_base.py       # Base testing utilities
│   └── utils.py           # Shared helpers (logging, timing, etc.)
│
└── templates/
    ├── algo_template.py   # Template for future algorithms
    ├── README_template.md # Template for per-algorithm documentation
    └── test_template.py   # Template for tests
```

No deviations without a strong reason.

---

## 3. Language & Tooling Rules

### Primary Language

* **Python 3.10+** (non-negotiable)

### Optional Secondary Language

* **C++** only if performance comparison is meaningful

### Prohibited

* Copy-pasting full solutions from the internet
* Using libraries that directly solve the algorithm
* Skipping mathematical explanation

---

## 4. Coding Standards

### File Rules

* One algorithm = one folder (later stages)
* One main implementation file
* One README per algorithm

### Code Rules

* Explicit variable names (no `x`, `tmp`, `foo`)
* Type hints everywhere
* No magic numbers
* Time & space complexity must be stated

### Example

```python
class AlgorithmBase:
    def run(self, input_data):
        raise NotImplementedError
```

---

## 5. Documentation Standards

Every algorithm README **must** include:

1. Problem statement (in your own words)
2. Constraints
3. Naive approach
4. Optimized approach
5. Mathematical reasoning
6. Time & space complexity
7. Edge cases
8. Example walkthrough

If any section is missing, the algorithm is incomplete.

---

## 6. Mathematics Prerequisites Checklist

You are expected to revise (not learn from scratch):

* Big-O, Big-Ω, Big-Θ
* Logarithms and exponent rules
* Arithmetic series & geometric series
* Recursion trees
* Proof by induction (basic)
* Modular arithmetic

If you cannot explain these **without notes**, pause progress.

---

## 7. Ban List (Strict)

You are **not allowed** to:

* Use `itertools.permutations` for permutation problems
* Use `heapq` without implementing a heap once
* Use `collections.Counter` before writing frequency logic manually
* Use `networkx` for graph algorithms

Reason: convenience kills understanding.

---

## 8. Testing Philosophy

* Tests are mandatory
* Edge cases > happy paths
* At least one adversarial input per algorithm

Testing answers the question:

> “How do I know this doesn’t silently fail?”

---

## 9. Evaluation Criteria (For Yourself)

An algorithm is considered **done** only if:

* You can explain it on a whiteboard
* You can derive complexity without memorization
* You can modify it under new constraints

If not, redo it.

---

## 10. Exit Criteria for Stage 0

You may move to Stage 1 only when:

* Folder structure is complete
* Base classes exist
* Templates are written
* This README is finalized
* You can articulate the purpose of the project clearly

Rushing past Stage 0 guarantees shallow mastery.

---

**Stage 0 is discipline. Respect it.**
