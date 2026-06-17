# 📝 Terminal Quiz Engine System

A robust, terminal-based application framework built in Python to parse external databases, manage session generation, handle custom schemas, and track live user metrics.

---

## ⚙️ Architecture & Logic Flow

The system operates on an automated multi-step pipeline. It reads raw string arrays from local files, maps them into index-safe hash matrices, and generates non-repeating data matrices for user consumption.

* **Step 1:** Read unstructured string data from a local flat file.
* **Step 2:** Parse and chunk continuous text rows sequentially into dictionary objects.
* **Step 3:** Generate a dynamic array sample to deliver distinct user query instances.

---

## 🚀 Key Features

* **External Database Engine:** Dynamically processes an unstructured flat-text array file (`question_bank.txt`) using systematic step jumps (`range(0, len(lines), 6)`).
* **Deterministic Session Slicing:** Uses high-entropy mathematical randomization (`random.sample`) to extract isolated, unique subsets of exactly 20 elements from a larger dataset.
* **Input Isolation & Validation Layer:** Employs an endless conditional catch loop (`while True`) that intercepts incorrect keystrokes, completely isolating data errors without breaking the main runtime execution loop.
* **Graceful Lifecycle Terminations:** Integrates low-level runtime handles (`sys.exit()`) to safely dump script runtimes on consumer abort requests.

---

## 🗃️ Database Schema (`question_bank.txt`)

To prevent parsing errors or out-of-bounds pointer crashes, the external text database must follow a strict **6-line repetition block** for each individual question object:

```text
Line 1: Question Stem Text
Line 2: Option A Value
Line 3: Option B Value
Line 4: Option C Value
Line 5: Option D Value
Line 6: Correct Key Identifier (Single character: a, b, c, or d)