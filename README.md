# Dharani-Hegde

## Programming Test - First Screening

This repository contains my solutions for the programming test's first screening stage.

## Programming Language Used: Python

## How to Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dharanihegde/Dharani-Hegde.git
   cd Dharani-Hegde
   ```

2. **Run any problem**:
   ```bash
   python Problem-1.py  # For Calculator
   python Problem-2.py  # For Odd Number Series
   python Problem-3.py  # For Pattern-based Odd Series
   python Problem-4.py  # For Multiple Counter
   ```

---

## Problem-1: Calculator Class

### Description
A simple calculator that performs basic arithmetic operations (Addition, Subtraction, Multiplication, and Division) using a class-based implementation.

### Features
- **Object-Oriented Design**: Clean Calculator class with separate methods for each operation
- **Multiple Input Formats**: Supports operation names (`add`, `multiply`) and symbols (`+`, `*`)
- **Error Handling**: Proper handling of division by zero and invalid operations
- **Two Modes**:
  - **Interactive Mode**: User-friendly interface with input validation
  - **Auto Test Mode**: Automated testing with predefined test cases

### How to Run

```bash
python Problem-1.py
```

Select a mode:
- Press `1` for Interactive Mode (manual input)
- Press `2` for Auto Test Mode (runs test cases)
- Press `3` to Exit

### Interactive Mode Usage

```
Enter first number (a): 10.5
Enter second number (b): 5.5
Enter operation (add or subtract or multiply or divide or + or - or * or /): add

Result: 10.5 add 5.5 = 16.0
--------------------------------------------------

Do you want to perform another calculation? (yes/no): no
```

### Supported Operations
- **Addition**: `add`, `+`
- **Subtraction**: `subtract`, `-`
- **Multiplication**: `multiply`, `*`
- **Division**: `divide`, `/`

### Input Specifications
- **a**: double (floating-point number)
- **b**: double (floating-point number)
- **operation**: string (operation name or symbol)

## Problem-2: Odd Number Series Generator

### Description
A program that generates the first 'a' odd numbers based on user input, where 'a' is a positive integer.

### Features
- **Simple and Efficient**: Uses mathematical formula to generate odd numbers
- **Input Validation**: Ensures only valid positive integers are accepted
- **Clean Output**: Formats the series as comma-separated values
- **Continuous Operation**: Loop allows multiple series generations

### How to Run

```bash
python Problem-2.py
```

### Usage Example

```
===================================================
ODD NUMBER SERIES GENERATOR
===================================================
This program generates the first 'a' odd numbers.
===================================================

Enter value of 'a' (positive integer): 4

Input a = 4
Output: 1, 3, 5, 7
--------------------------------------------------

Generate another series? (yes/no): yes

Enter value of 'a' (positive integer): 10

Input a = 10
Output: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
--------------------------------------------------

Generate another series? (yes/no): no

Goodbye!
```

### Pattern Explanation
- Input a = 1 -> Output: 1
- Input a = 2 -> Output: 1, 3
- Input a = 3 -> Output: 1, 3, 5
- Input a = 4 -> Output: 1, 3, 5, 7
- Input a = x -> Output: First x odd numbers

### Technical Details
- **Algorithm**: Uses formula `2*i - 1` where i ranges from 1 to a
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Edge Cases**: Returns empty output for non-positive integers

## Problem-3: Pattern-based Odd Number Series

### Description
A program that generates odd numbers following a specific pattern where even inputs produce the same output as the previous odd input.

### Pattern Rule
- **If 'a' is odd**: Generate 'a' odd numbers
- **If 'a' is even**: Generate 'a-1' odd numbers (same as previous odd)

### Features
- **Pattern Recognition**: Automatically applies the even/odd rule
- **Input Validation**: Ensures only valid positive integers are accepted
- **User-Friendly**: Continuous operation with clear prompts

### How to Run

```bash
python Problem-3.py
```

### Usage Example

```
===================================================
PATTERN-BASED ODD NUMBER SERIES GENERATOR
===================================================
Pattern: Even inputs give same output as previous odd
===================================================

Enter value of 'a' (positive integer): 3

Input a = 3
Output: 1, 3, 5
--------------------------------------------------

Generate another series? (yes/no): yes

Enter value of 'a' (positive integer): 4

Input a = 4
Output: 1, 3, 5
--------------------------------------------------

Generate another series? (yes/no): yes

Enter value of 'a' (positive integer): 5

Input a = 5
Output: 1, 3, 5, 7, 9
--------------------------------------------------

Generate another series? (yes/no): no

Goodbye!
```

### Pattern Examples
- Input a = 1 -> Output: 1
- Input a = 2 -> Output: 1 (same as a=1)
- Input a = 3 -> Output: 1, 3, 5
- Input a = 4 -> Output: 1, 3, 5 (same as a=3)
- Input a = 5 -> Output: 1, 3, 5, 7, 9
- Input a = 6 -> Output: 1, 3, 5, 7, 9 (same as a=5)

### Technical Details
- **Algorithm**: Uses modulo operator to detect even/odd: `count = a if a % 2 == 1 else a - 1`
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Pattern Logic**: Even numbers produce output of `a-1` odd numbers

## Problem-4: Multiple Counter Dictionary

### Description
A program that counts how many numbers in a given list are multiples of each number from 1 to 9, returning the results as a dictionary.

### Features
- **Comprehensive Counting**: Checks divisibility for all numbers 1-9
- **Flexible Input**: Accepts lists with or without brackets
- **Clean Output**: Returns dictionary in the exact required format
- **Input Validation**: Ensures only valid integers are processed

### How to Run

```bash
python Problem-4.py
```

### Usage Example

```
===================================================
MULTIPLE COUNTER DICTIONARY
===================================================
Count multiples of 1-9 in a list of numbers
===================================================

Example input formats:
  - 1,2,8,9,12,46,76,82,15,20,30
  - [1,2,8,9,12,46,76,82,15,20,30]

Enter list of numbers (comma-separated): 1,2,8,9,12,46,76,82,15,20,30

Input: [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
Output: {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
--------------------------------------------------

Analyze another list? (yes/no): yes

Enter list of numbers (comma-separated): [10, 20, 30, 40, 50]

Input: [10, 20, 30, 40, 50]
Output: {1: 5, 2: 5, 3: 1, 4: 2, 5: 5, 6: 1, 7: 0, 8: 1, 9: 0}
--------------------------------------------------

Analyze another list? (yes/no): no

Goodbye!
```

### Algorithm Explanation
For each number from 1 to 9, the program:
1. Iterates through the input list
2. Checks if each number is divisible using modulo operator (`%`)
3. Counts the total multiples found
4. Stores the count in a dictionary with the divisor as key

### Output Interpretation
For input `[1,2,8,9,12,46,76,82,15,20,30]`:
- `1: 11` → All 11 numbers are divisible by 1
- `2: 8` → 8 numbers are even (divisible by 2)
- `3: 4` → 4 numbers are divisible by 3
- `7: 0` → No numbers are divisible by 7
- And so on for each key from 1 to 9

### Technical Details
- **Time Complexity**: O(9n) = O(n) where n is the length of input list
- **Space Complexity**: O(1) - fixed size dictionary with 9 keys
- **Input Formats**: Accepts both `1,2,3` and `[1,2,3]` formats
- **Output Format**: Dictionary with keys 1-9 and their respective counts

### Requirements
- Python 3
- No external dependencies required

### Author
Dharani Hegde

### Date
27th June 2025
