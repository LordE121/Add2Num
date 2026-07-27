# Add2Num - MyBigNumber

Object-oriented Python implementation for adding two large non-negative integers represented as strings. The algorithm scans both strings from right to left, adds each pair of digits, stores the result digit, and carries the remainder exactly like primary-school addition.

## Requirements

- Python 3.9 or newer
- No third-party dependencies

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

From the project root, pass the two number strings as positional arguments:

```bash
python main.py 1234 897
```

Expected output:

```text
2131
```

To show each addition step while still printing the final result, add `--log`:

```bash
python main.py 99 1 --log
```

## Enable operation logging in code

The core function logs each addition step through Python's `logging` module.

```python
import logging
from my_big_number import MyBigNumber

logging.basicConfig(level=logging.INFO, format="%(message)s")
MyBigNumber().sum("1234", "897")
```

## Run tests

From the project root, run:

```bash
python -m unittest -v
```

Expected result: all tests pass.

## Version for evaluation

The completed Task 1 version should be published as `0.0.1` by using a Git tag or branch, depending on the Git server workflow.
