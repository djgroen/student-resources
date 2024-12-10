# Software Engineering Basics and Good Practices

## How to report technical problems
* Before reporting a problem, always make sure that you have examined the existing documentation. Check the installation manuals and user guides of the relevant tool(s), and also check this repository for helpful information first.
* Always write specifically what you are trying to accomplish, and what you are doing to accomplish it.
* Copy/paste a direct screenshot, command list or code fragment of the stuff you are doing.
* Copy/paste error output *directly*, or take a screenshot if that is not possible.
* Raise technical problems in the #technicalissues channel on the 42Brunel slack, raise them as "Issues" on GitHub only if you are 100% certain that it's a code issue.

## Writing Unit Tests

Unit tests are a crucial aspect of software development, enabling developers to verify that individual components of their code function correctly. This guide provides an overview of best practices for writing unit tests, along with insights on using multiple assertions effectively.

---

### What is a Unit Test?

A unit test is a piece of code that tests a specific function or method in isolation from the rest of the application. The primary goal is to validate that each unit of the software performs as expected, which helps catch bugs early in the development process.

---

### Best Practices for Writing Unit Tests

#### 1. Keep Tests Focused

While it's possible to have multiple assertions within a single test, consider the following:

- **Clarity on Failures**: If a test fails, it should be clear to the user what went wrong. Avoid combining multiple assertions that might obscure the cause of the failure.

- **Simplicity**: Strive for simplicity in your tests to make them easier to understand and maintain. This will benefit both you and other developers who may work with your code.

#### 2. Use Descriptive Names

Make sure your test function names clearly indicate what is being tested. This helps others understand the purpose of the test without needing to read the implementation details.

#### 3. Write Custom Print Functions for Test Results

To simplify the process of reporting test outcomes, you can create a custom print function. This function can provide clear output and allow for easy adjustments to verbosity across all your tests.

#### Example: Custom Print Function

Here’s a simple implementation of a custom print function in Python:

```python
def pr_unittest(test_name, test_outcome_bool):
    """Print the outcome of a unit test.
    
    Args:
        test_name (str): The name of the test.
        test_outcome_bool (bool): The result of the test (True for pass, False for fail).
    """
    if not test_outcome_bool:
        print(f"Test '{test_name}' failed.")
    else:
        # You can choose to suppress output for passing tests if desired.
        pass
```

#### 4. Document Your Findings

Documenting your unit testing results is essential for tracking test outcomes and ensuring that all tests are accounted for. A well-structured documentation approach can help you identify which tests passed, which failed, and any related issues. 

##### Example Documentation Table

Consider using a table to record your findings. Below is a simple template you can follow:

| Test Name         | Description                     | Outcome | Notes                            |
|-------------------|---------------------------------|---------|----------------------------------|
| Sum Test          | Tests the sum function with 2+3 | Passed  | Function works as expected.     |
| Product Test      | Tests the product function with 2*3 | Passed  | Function works as expected.     |
| Edge Case Test    | Tests sum with negative numbers | Failed  | Returns incorrect result; need to fix. |

##### Key Components of the Table:

- **Test Name**: The name of the test function.
- **Description**: A brief description of what the test is validating.
- **Outcome**: Whether the test passed or failed.
- **Notes**: Any additional comments about the test, such as reasons for failure or insights for improvements.

This structured approach allows you to maintain clear records of your unit tests, making it easier to communicate findings to your team and prioritize future work based on test results.

## Coding with PEP 8 Guidelines

### What is PEP 8?
* PEP 8 is the official style guide for Python code. It provides conventions for writing clean, readable, and maintainable code.
* Following PEP 8 makes your code easier to understand and collaborate on with others, ensuring consistency across projects.


### Key Guidelines from PEP 8

#### 1. **Indentation**
* Use 4 spaces per indentation level. Do not use tabs.
```python
# Correct:
def example_function():
    print("Hello, World!")

# Incorrect:
def example_function(): 
    print("Hello, World!")  # Uses tabs
```
#### 2. **Line Length**
* Limit all lines to a maximum of 79 characters.
* For comments or docstrings, limit lines to 72 characters.
```python
# Correct:
def example_function(argument):
    print(f"Argument value is: {argument}")

# Incorrect:
def example_function(argument): print(f"Argument value is: {argument}")  # Too long
```
#### 3. **Blank Lines**
* Use blank lines to separate functions, classes, and logical sections of code.
* Use two blank lines before top-level functions or class definitions, and one blank line inside functions to separate logic.

#### 4. **Naming Conventions**
* Use descriptive and readable names for variables, functions, and classes:
    - Function names: snake_case
    - Variable names: snake_case
    - Class names: CamelCase
```python
# Correct:
class MyClass:
    def my_function(self):
        my_variable = 10

# Incorrect:
class myclass:
    def MyFunction(self):
        MyVariable = 10
```
#### 5. Imports
* Group imports into three sections, separated by blank lines:
  1. Standard library imports.
  2. Third-party library imports.
  3. Local application imports.
* Avoid wildcard imports (e.g., `from module import *`).
```python
# Correct:
import os import sys

import numpy as np import pandas as pd

from myproject import mymodule
```
#### 6. Spacing
* Avoid extra spaces in expressions or statements.
```python
# Correct:
result = x * (y + z)
# Incorrect:
result = x * ( y + z )
```
#### 7. Comments
* Write clear and concise comments that explain the "why," not just the "what."
* Use `#` for inline comments and triple quotes for docstrings.
```python
def calculate_area(length, width): """Return the area of a rectangle.""" 
return length * width
```

