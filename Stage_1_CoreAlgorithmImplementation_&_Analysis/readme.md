# Stage 1 — Core Algorithm Implementation & Analysis

## Purpose of Stage 1

Stage 1 exists to eliminate shallow understanding. This stage forces you to **implement, analyze, and justify** fundamental algorithms from scratch. The goal is not speed or quantity—it is correctness, clarity, and intellectual discipline.

If Stage 0 was about setup and structure, **Stage 1 is about execution and reasoning**.

You are expected to think like a computer scientist, not a tutorial follower.

---

## Learning Objectives (Non‑Negotiable)

By the end of Stage 1, you must be able to:

* Implement core algorithms without library shortcuts
* Explain *why* an algorithm works, not just how
* Analyze worst‑case and average‑case time complexity
* Identify when an algorithm **should not** be used
* Handle edge cases deliberately, not accidentally

If you cannot defend your design decisions verbally or on paper, Stage 1 is **not complete**.

---

## Scope of Stage 1

You will implement algorithms from the following categories:

1. Arrays / Prefix / Two Pointers
2. Sorting Algorithms
3. Searching Algorithms
4. Recursion & Divide‑and‑Conquer
5. Basic Greedy Algorithms

Advanced data structures (trees, graphs, DP, hashing internals) are **explicitly out of scope**.

---

## Mandatory Algorithms

### Arrays / Prefix

* Prefix Sum (1D)
* Sliding Window (fixed and variable size)
* Two‑pointer techniques

### Sorting

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort (Lomuto or Hoare — choice must be justified)

### Searching

* Linear Search
* Binary Search (iterative)
* Binary Search (recursive)
* Binary Search on Answer (parametric search)

### Recursion / Divide & Conquer

* Factorial (baseline recursion)
* Power(x, n) with logarithmic recursion
* Merge Sort (recursive focus)

### Greedy

* Activity Selection
* Minimum Coins (canonical system only — limitation must be documented)

Skipping any of the above means Stage 1 is incomplete.

---

## Folder Structure

```
stage-1/
│
├── README.md
│
├── base/
│   ├── algorithm.py      # Abstract base class / interface
│   ├── utils.py          # Timers, random input generators
│
├── arrays/
│   ├── prefix_sum.py
│   ├── sliding_window.py
│   └── readme.md
│
├── sorting/
│   ├── bubble.py
│   ├── selection.py
│   ├── insertion.py
│   ├── merge.py
│   ├── quick.py
│   └── readme.md
│
├── searching/
│   ├── linear.py
│   ├── binary.py
│   └── readme.md
│
├── recursion/
│   ├── factorial.py
│   ├── power.py
│   └── readme.md
│
├── greedy/
│   ├── activity_selection.py
│   ├── min_coins.py
│   └── readme.md
│
└── tests/
    ├── test_sorting.py
    ├── test_searching.py
    └── edge_cases.md
```

Clean structure is mandatory. Sloppy organization reflects sloppy thinking.

---

## Rules & Constraints

1. **No built‑in algorithm shortcuts** (`sort()`, `bisect`, etc.)
2. Every algorithm file must include:

   * Problem definition
   * Algorithm intuition
   * Step‑by‑step logic
   * Time complexity (best, average, worst if applicable)
   * Space complexity
   * Edge cases
   * Known limitations
3. Every algorithm must:

   * Handle empty input
   * Handle single‑element input
   * Be tested against worst‑case input
4. Code must be readable and deterministic

Violating these rules means you are missing the point of the stage.

---

## Testing Requirements

Each algorithm must be validated against:

* Empty input
* Minimum valid input
* Large input (simulated)
* Known failure or limitation cases

Tests should **break bad implementations**, not merely confirm good ones.

---

## Evaluation Criteria

You pass Stage 1 only if:

* All mandatory algorithms are implemented
* All tests pass without hacks or special‑case code
* You can explain trade‑offs between algorithms
* You can identify incorrect use‑cases for each algorithm
* Code is consistent, clean, and documented

Confidence without proof does not count.

---

## Common Failure Modes (Avoid These)

* Memorizing implementations without understanding
* Ignoring edge cases
* Copy‑pasting from tutorials
* Treating complexity analysis as optional
* Rushing to “advanced topics” prematurely

If you do any of the above, stop and restart Stage 1 properly.

---

## Exit Condition

You are allowed to move to **Stage 2 (Data Structures)** only when:

* You can derive each algorithm from first principles
* You can compare algorithms analytically
* You can reason about performance before coding

Stage 1 is not about finishing fast.
It is about **building a foundation that does not crack later**.
