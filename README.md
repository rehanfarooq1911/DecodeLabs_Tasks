# DecodeLabs Python Tasks

A collection of beginner-friendly Python projects completed during the **DecodeLabs Python Programming** industrial training (Batch 2026). Each task is a standalone command-line program that uses only the Python standard library, so no installation is needed beyond Python itself.

## Projects

| Task | Project | File |
|------|---------|------|
| 1 | To-Do List | `task1.py` |
| 2 | Expense Tracker | `task2.py` |
| 3 | Random Password Generator | `task3.py` |
| 4 | General Knowledge Quiz | `task4.py` |

---

## Task 1: To-Do List

A menu-driven program for managing a list of tasks during a session.

**Features**
- Add a task, view all tasks, or exit from a simple menu
- Tasks are shown as a numbered list using `enumerate()`
- Empty or whitespace-only tasks are rejected
- Invalid menu choices are handled without crashing

**Concepts used:** lists, `append()`, `enumerate()`, functions, `while` loops, `if-elif-else`, input/output

> Tasks are stored in memory only, so the list is cleared when the program exits.

---

## Task 2: Expense Tracker

Keeps a running total of the expenses a user enters and prints the final total when they finish.

**Features**
- Enter expenses one at a time and type `quit` to stop
- Running total is shown after every entry
- Defensive input handling: non-numeric, `nan`/`inf`, zero and negative values are rejected
- Prints the number of transactions and the final total in a currency format (e.g. `$1,250.50`)

**Concepts used:** accumulator pattern (`total += expense`), `while True` loop with a sentinel value, `try/except ValueError`, string formatting

---

## Task 3: Random Password Generator

Generates a strong random password of a length chosen by the user and reports its strength.

**Features**
- Password length must be between 8 and 64 characters
- Uses letters, digits and punctuation
- Built with Python's `secrets` module, which is designed for security-sensitive randomness, instead of `random`
- Displays the password's entropy in bits as a strength indicator
- Re-prompts on invalid input (non-integer, too short, too long)

**Concepts used:** `secrets`, `string`, `math.log2`, loops, `try/except`, f-strings

---

## Task 4: General Knowledge Quiz

A three-question quiz that keeps score and prints the final result.

**Features**
- Asks 3 general knowledge questions
- Answers are trimmed and lower-cased, so `"  PaRiS  "` is accepted
- +1 point for each correct answer; the correct answer is shown when the user is wrong
- Final score is displayed as `score/3`

**Concepts used:** `if-else` logic, variables, string methods (`.strip()`, `.lower()`), f-strings

---

## How to Run

Make sure Python 3 is installed, then run any task from the terminal:

```bash
python task1.py   # To-Do List
python task2.py   # Expense Tracker
python task3.py   # Password Generator
python task4.py   # General Knowledge Quiz
```

## Requirements

- Python 3.6 or higher
- No external libraries

## Author

Muhammad Rehan Farooq 
[@rehanfarooq1911](https://github.com/rehanfarooq1911)
