# Add2Num - MyBigNumber

Add2Num is a small Python project for adding two very large non-negative integers stored as strings.

The code follows the same method taught in primary school:

1. Read both numbers from right to left.
2. Add the two current digits and the remembered carry.
3. Store the result digit.
4. Carry `1` to the next step when needed.
5. Reverse the stored digits to get the final answer.

Example: `1234 + 897 = 2131`.

## Requirements

### Runtime

- Python 3.9 or newer
- No external runtime packages

### Testing

- `pytest` from `requirements.txt`

## Project structure

```text
Add2Num/
├── main.py                    # Interactive CLI program
├── my_big_number.py           # MyBigNumber class and core algorithm
├── tests/
│   └── test_my_big_number.py  # Pytest tests
├── README.md                  # Usage guide
├── requirements.txt           # Test dependencies
├── .gitignore                 # Ignored local/generated files
└── LICENSE                    # Project license
```

## Use as a class

```python
from my_big_number import MyBigNumber

calculator = MyBigNumber()
print(calculator.sum("1234", "897"))  # 2131
```

## Print operation history

Use `show_steps=True` when you want to see each addition step:

```python
from my_big_number import MyBigNumber

calculator = MyBigNumber(show_steps=True)
print(calculator.sum("99", "1"))
```

Example output:

```text
Step 1: 9 + 1 + carry 0 = 10; write 0, next carry 1
Step 2: 9 + 0 + carry 1 = 10; write 0, next carry 1
Step 3: 0 + 0 + carry 1 = 1; write 1, next carry 0
Result: 99 + 1 = 100
100
```

## Run as CLI

Run the interactive CLI from the project root:

```bash
python main.py
```

Then enter the two numbers when prompted:

```text
First number: 1234
Second number: 897
2131
```

The CLI intentionally stays simple and uses only Python core features such as `input()` and `print()`.

## Run tests

Install test dependencies:

```bash
pip install -r requirements.txt
```

Run the pytest suite:

```bash
pytest -v
```

Expected result: all tests pass.

## Version for evaluation

Publish the completed Task 1 version as `0.0.1` using the branch or tag workflow required by your Git server.
