# Machine Learning Algorithms From-Scratch 

A lifelong, research-grade project to implement machine learning, deep learning, and probabilistic models **from first principles**, following the **historical evolution of the field (1920 → present)**, with strict mathematical rigor and zero framework magic.

This repository prioritizes **understanding over convenience**, **explicit computation over abstraction**, and **verification over claims**.

---

## 1. Project Goals

The goals of this repository are:

- To rebuild ML systems **from the ground up**, not by imitation but by derivation
- To treat **math, code, experiments, and failure analysis** as first-class artifacts
- To follow a **chronological learning path** aligned with how the field actually evolved
- To develop deep intuition about:
  - numerical stability
  - optimization
  - gradients and backpropagation
  - probabilistic reasoning
  - ML system design

This is **not** a framework clone, tutorial collection, or benchmarking suite.

---

## 2. Core Principles (Non-Negotiable)

1. Correctness before performance
2. Explicit computation before abstraction
3. Mathematical derivation before implementation
4. Verification before trust
5. Learning depth before speed

If an algorithm “just works” without explanation, it does not belong here.

---

## 3. What This Repository Is NOT

- Not a PyTorch / TensorFlow reimplementation
- Not a shortcuts-based NumPy demo repo
- Not a notebook dump
- Not a black-box ML collection
- Not optimized for production or benchmarks

---

## 4. Technology Stack

### Allowed

- Python (reference implementations)
- NumPy (numerical storage + basic arithmetic only)
- C++ (memory, kernels, systems understanding)
- pybind11 (late stages only)

### Globally Banned Libraries

```
torch
tensorflow
jax
scipy
sklearn
autograd libraries
numba
cupy
einops
optax
```

### Globally Banned NumPy APIs

```
np.linalg.*
np.einsum
np.solve
np.inv
np.pinv
np.svd
np.qr
np.fft*
automatic differentiation tools
```

NumPy is treated as a **dumb calculator**, not a reasoning engine.

---

## 5. Historical Roadmap

The project is divided into chronological stages:

| Stage   | Era          | Focus                               |
| ------- | ------------ | ----------------------------------- |
| Stage-0 | 1920–1930    | Numerical & statistical foundations |
| Stage-1 | 1930–1950    | Linear algebra as computation       |
| Stage-2 | 1950–1960    | Optimization                        |
| Stage-3 | 1960–1970    | Probability & statistics            |
| Stage-4 | 1970–1985    | Classical machine learning          |
| Stage-5 | 1985–2005    | Autograd & backpropagation          |
| Stage-6 | 2005–2012    | Deep feedforward networks           |
| Stage-7 | 2012–2016    | CNNs & sequence models              |
| Stage-8 | 2016–Present | Probabilistic DL & ML systems       |

Each stage has:

- a strict ban list
- defined exit criteria
- zero dependency on future stages

---

## 6. Repository Structure

```
from-scratch-ml/
from-scratch-ml/
│
├── README.md
├── CONTRIBUTING.md
├── STAGES.md
│
├── stage-0_numerical_foundations/
├── stage-1_linear_algebra/
├── stage-2_optimization/
├── stage-3_probability/
├── stage-4_classical_ml/
├── stage-5_autograd/
├── stage-6_deep_learning/
├── stage-7_structured_models/
└── stage-8_systems/
Folder names are final. Renaming is forbidden.
```

## 7. Standard Stage Structure

Each stage follows this structure:

```
stage-X_name/
│
├── README.md # Stage goals, bans, exit criteria
stage-X_name/
│
├── README.md # Stage goals, bans, exit criteria
│
├── base/ # Reusable primitives only
│
├── algorithms/
│ └── algorithm_name/
│ ├── main.py # Minimal runnable example
│ ├── project.py # Mini-project / experiment
│ ├── tests.py
│ └── README.md # Math, bans, theory, failures
│
├── cpp/ # Only if justified
├── math/ # Derivations, proofs
├── verification/ # Hand checks, comparisons
├── videos/ # Scripts and references
└── tests/ # Stage-level tests
```

## 8. Algorithm Completion Criteria

An algorithm is considered complete **only if** all of the following exist:

1. Mathematical derivation (written)
2. Explicit forward computation
3. Explicit backward computation (if applicable)
4. Numerical gradient verification
5. Edge-case and failure tests
6. A mini-project using real data
7. Documentation explaining why it fails

Missing any item → algorithm is incomplete.

---

## 9. Python vs C++ Policy

- Python is the reference implementation
- C++ is introduced only when it teaches:
  - memory layout
  - performance tradeoffs
  - systems boundaries

Rules:

- Python must exist before C++
- C++ must conceptually mirror Python
- If results differ, C++ is wrong

---

## 10. Notebook Policy

Jupyter notebooks are discouraged.

Allowed only for:

- visualization
- numerical instability demonstrations
- experiments

Every notebook must have:

- a paired `.py` implementation
- no hidden logic

---

## 11. Contribution Rules

- One concept per commit
- One algorithm per branch
- No bulk commits
- No unexplained refactors
- Commit messages explain **why**, not what

Violating bans invalidates the contribution.

---

## 12. Intended Audience

This repository is for:

- long-term learners
- systems-oriented thinkers
- research-focused engineers
- people who value understanding over shortcuts

It is not for:

- framework users
- quick demos
- performance chasers

---

## 13. Final Note

This project is intentionally:

- slow
- strict
- uncomfortable at times

That is the cost of genuine understanding.

If executed honestly, this repository will represent **years of accumulated knowledge**, not copied skill.

