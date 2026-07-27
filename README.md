# Add2Num - MyBigNumber

Object-oriented Python implementation for adding two large non-negative integers represented as strings. The algorithm scans both strings from right to left, adds each pair of digits, stores the result digit, and carries the remainder exactly like primary-school addition.

## Requirements

- Python 3.9 or newer
- pytest for running tests

## Project structure

```text
Add2Num/
├── main.py                    # CLI program
├── my_big_number.py           # MyBigNumber class
├── tests/
│   └── test_my_big_number.py  # Unit tests
├── README.md                  # Usage guide
├── requirements.txt           # Dependency list
├── .gitignore                 # Ignored local/generated files
└── LICENSE                    # Project license
```

## Use as a class

```python
from my_big_number import MyBigNumber

calculator = MyBigNumber()
print(calculator.sum("1234", "897"))  # 2131
```

## Run as CLI

From the project root, run the interactive CLI and enter the two number strings when prompted:

```bash
python main.py
```

Expected output:

```text
2131
```

To print each addition step from code, pass `show_steps=True`:

```python
from main import main

main("99", "1", show_steps=True)
```

The implementation uses only Python core features and does not require external packages.

## Print operation history in code

The core function can print each addition step without importing extra modules.

```python
from my_big_number import MyBigNumber

MyBigNumber(show_steps=True).sum("1234", "897")
```

## Run tests

Install test dependencies if needed:

```bash
pip install -r requirements.txt
```

From the project root, run:

```bash
pytest -v
```

Expected result: all tests pass.

## Version for evaluation

The completed Task 1 version should be published as `0.0.1` by using a Git tag or branch, depending on the Git server workflow.
