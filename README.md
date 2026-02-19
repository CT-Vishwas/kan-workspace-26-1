# Python Learning & Practice Repository

This repository contains Python files demonstrating various programming concepts, from fundamentals to advanced topics. Each file is a self-contained example with clear implementations and use cases.

---

## Table of Contents

1. [Fundamentals & Basic Concepts](#fundamentals--basic-concepts)
2. [Object-Oriented Programming](#object-oriented-programming)
3. [Advanced Python Concepts](#advanced-python-concepts)
4. [File & Data Handling](#file--data-handling)
5. [Jupyter Notebooks](#jupyter-notebooks)

---

## Fundamentals & Basic Concepts

### `first.py` - Simple Interest Calculation

**Purpose:** Demonstrates basic arithmetic operations and formula implementation.

**Concept:** Calculates simple interest using the formula: SI = (Principal × Time × Rate) / 100

**Key Features:**
- Variable assignment and initialization
- Mathematical operations
- Output formatting with `print()`

**Code Explanation:**
```python
principal = 1000           # Amount of money
time_in_months = 36        # Time period
rate_of_interest = 0.07    # Interest rate (7%)

# Calculate simple interest
simple_interest = (principal * time_in_months * rate_of_interest) / 100
print('Simple Interest is:', simple_interest)
```

**Use Case:** Financial calculations, loan interest computation

**Output:** `Simple Interest is: 25.2`

---

### `third.py` - Loop with Input Handling

**Purpose:** Demonstrates loops and user input in Python.

**Concept:** Iterates through a loop accepting user input and performs calculations.

**Key Features:**
- `for` loops
- User input with `input()` function
- Variable initialization and updates

**Code Overview:**
```python
for i in range(5):
    num = float(input('Enter a number:'))
    total = 0
    num += total
    print("Total: ", total)
```

**Note:** This code has a logical issue - `total` is always initialized to 0 inside the loop, so the sum never accumulates. To fix it, `total` should be declared outside the loop.

---

## Object-Oriented Programming

### `demo_access.py` - Access Control with Properties

**Purpose:** Demonstrates data encapsulation using property decorators and private attributes.

**Concepts:**
- Private attributes (name mangling with `__`)
- `@property` decorator for getters
- `@setter` decorator for validation

**Key Features:**
- Encapsulation of balance attribute
- Property getter and setter methods
- Data validation in setters

**Code Example:**
```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (name mangling)

    def deposit(self, amount):
        self.__balance += amount

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = balance

# Usage
acc = Account("Alice", 1000)
acc.deposit(500)
print(acc.balance)  # Access via property
```

**Key Concepts:**
- `__balance`: Private attribute (read from external access)
- `@property`: Defines getter method, allows `acc.balance` syntax
- `@setter`: Defines setter, enforces validation (balance must be non-negative)

**Use Case:** Banking systems, financial applications requiring data validation

---

### `second.py` - Inheritance with `__slots__`

**Purpose:** Demonstrates class inheritance and memory optimization using `__slots__`.

**Concepts:**
- Class inheritance (`Person` → `User`)
- `__slots__` for memory efficiency
- `super()` for calling parent class methods

**Code Example:**
```python
class Person:
    __slots__ = ['name', 'city']  # Restrict attributes to these names
    def __init__(self, name, city):
        self.name = name
        self.city = city

class User(Person):
    def __init__(self, name, city, age):
        super().__init__(name, city)  # Call parent constructor
        self.age = age

# Usage
p1 = Person('vishwas', 'bangalore')
p2 = User('Arjun', 'bangalore', 23)
```

**Key Concepts:**
- `__slots__`: Restricts instances to only have the listed attributes, saving memory
- `super()`: Calls parent class methods safely
- Inheritance: Child class extends parent's functionality

**Important Note:** Line `p1.salary = 25000` would raise an `AttributeError` because `salary` is not in `__slots__`.

**Use Case:** Large-scale applications requiring memory optimization, OOP design patterns

---

### `demo_dataclasses.py` - Modern Data Structures with Pydantic

**Purpose:** Demonstrates data validation and structuring using the Pydantic library.

**Concepts:**
- Data validation using Pydantic's `BaseModel`
- Type hints for attribute definition
- Automatic validation on instantiation

**Code Example:**
```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    city: str
    age: int

# Usage
p1 = Person(name='vishwas', city='Bangalore', age='23')  # age is auto-converted to int
print(f'The Person is {p1.name}, his age is {p1.age}')
```

**Key Features:**
- Type hints: `name: str`, `city: str`, `age: int`
- Automatic type coercion: '23' (string) → 23 (integer)
- Data validation: Ensures data types are correct
- Built-in serialization for API responses

**Use Case:** REST APIs, data serialization, configuration management

---

## Advanced Python Concepts

### `demo_comprehensions.py` - Comprehensions, Map & Lambda

**Purpose:** Demonstrates advanced list/dictionary creation and functional programming techniques.

**Concepts:**
- List comprehensions
- Dictionary comprehensions
- `map()` function with lambda
- Filtering with comprehensions

**Code Examples:**

**1. List Comprehension:**
```python
# Create list of numbers 1-10
l1 = [i for i in range(1, 11)]
print(l1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create list of squares for even numbers
l3 = [i**2 for i in range(20) if i % 2 == 0]
```

**2. Dictionary Comprehension:**
```python
# Create dict of number -> square mapping
d1 = {k: k**2 for k in range(1, 11)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

**3. Map Function:**
```python
l1 = ['1', '2', '3', '4']
# Convert strings to integers
l2 = list(map(int, l1))

# Convert to integers with lambda
l2 = list(map(lambda x: int(x)**2, ['1', '2', '3']))  # [1, 4, 9]
```

**Key Differences:**
- **Comprehensions**: Pythonic, readable, often faster
- **Map**: Functional style, works with built-in functions and lambdas

**Use Case:** Data transformation, functional programming patterns, clean and efficient code

---

### `demo_decorators.py` - Function Decorators for Timing

**Purpose:** Demonstrates decorators for extend function behavior without modifying the original function.

**Concepts:**
- Function decorators
- `*args` and `**kwargs` for flexible arguments
- Timing function execution
- Wrapper functions

**Code Example:**
```python
import datetime

def func_timer(func):
    """Decorator that measures function execution time"""
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        print(f"The function ran for {duration}s")
        return result
    return wrapper

@func_timer  # Apply the decorator
def slow_func():
    for i in range(10000):
        print(i, end='')

# Usage
slow_func()  # Output: prints numbers and execution time
```

**How It Works:**
1. `func_timer` is a decorator function that takes a function as argument
2. `wrapper` is the inner function that does the timing
3. `@func_timer` syntax applies the decorator to `slow_func`
4. When `slow_func()` is called, it actually calls `wrapper(slow_func)`

**Use Cases:**
- Performance monitoring
- Logging function calls
- Authentication & authorization
- Caching/memoization

---

### `demo_fp.py` - Functional Programming Principles

**Purpose:** Demonstrates immutability and functional programming paradigms.

**Concepts:**
- Pure functions (no side effects)
- Immutability (not modifying original data)
- Function composition

**Code Example:**
```python
# Traditional approach (mutates global state)
orders = ['order1', 'order2']

def add_order_traditional(new_order):
    orders.append(new_order)  # Modifies original list
    
# Functional approach (pure function)
def add_order_fp(order_list, new_order):
    return order_list + [new_order]  # Returns new list

# Usage
orders = ['order1', 'order2']
new_orders = add_order_fp(orders, 'order3')
# orders remains ['order1', 'order2']
# new_orders is ['order1', 'order2', 'order3']
```

**Key Principles:**
- **Pure Functions**: Same input always produces same output, no side effects
- **Immutability**: Original data is never modified
- **Referential Transparency**: Functions can be replaced with their return values

**Benefits:**
- Easier to test (no hidden state changes)
- Better for concurrent/parallel programming
- More predictable code behavior

---

## File & Data Handling

### `demo_files.py` - File I/O with Exception Handling

**Purpose:** Demonstrates reading files safely with proper exception handling.

**Concepts:**
- `with` statement (context manager)
- Exception handling (`try-except`)
- File reading methods

**Code Example:**
```python
try:
    with open('data.txt', 'r') as fp:
        data = fp.read()
        print(data)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Unknown Error:", str(e))
```

**Key Features:**
- `with` statement: Automatically closes file (resource management)
- `try-except`: Handles potential errors gracefully
- `FileNotFoundError`: Specific exception for missing files

**Code Modes:**
- `'r'`: Read (default)
- `'w'`: Write (overwrites)
- `'a'`: Append
- `'b'`: Binary mode

**Best Practices:**
- Always use `with` statement for file operations
- Catch specific exceptions first, then generic ones
- Close files properly (automatic with `with`)

**Use Case:** Data import, log file reading, configuration file parsing

---

### `demo_csv.py` - CSV File Handling

**Purpose:** Demonstrates reading and processing CSV files using the `csv` module.

**Concepts:**
- CSV reading with `csv.reader`
- Dictionary-based reading with `csv.DictReader`
- Error handling for file operations

**Code Example:**
```python
import csv

try:
    with open('employee_data.csv', 'r') as fp:
        # Method 1: List-based
        # data = csv.reader(fp)
        # for row in data:
        #     print(row[0])
        
        # Method 2: Dictionary-based (recommended)
        data = csv.DictReader(fp)
        print(data.fieldnames)  # Column headers
        for row in data:
            print(row['NAMES'])  # Access by column name
            
except FileNotFoundError:
    print("File Not Found")
```

**Comparison:**
- **`csv.reader`**: Returns lists, access by index: `row[0]`
- **`csv.DictReader`**: Returns OrderedDict, access by name: `row['NAMES']`

**Advantages of DictReader:**
- More readable: named columns instead of indices
- Robust to column order changes
- Better for data validation

**Use Case:** Data analysis, ETL processes, employee data management

---

### `utils.py` - Utility Functions

**Purpose:** Contains reusable utility functions for the project.

**Concepts:**
- Function definition and reuse
- String manipulation
- Module structure

**Code Example:**
```python
def username_extracter(email_id):
    """
    Extracts username from email address.
    
    Args:
        email_id (str): Email address
        
    Returns:
        str: Username part before '@' symbol
        
    Example:
        >>> username_extracter('vishwas@cloudthat.com')
        'vishwas'
    """
    return email_id[:email_id.find('@')]

if __name__ == '__main__':
    email = 'vishwas@cloudthat.com'
    username = username_extracter(email)
    print(f"The user name of {email} is {username}")
```

**Key Concepts:**
- `find()`: Locates substring position, returns -1 if not found
- String slicing: `email_id[:pos]` gets characters before position
- Docstring: Documents function purpose, arguments, and return value
- `if __name__ == '__main__'`: Runs code only when file is executed directly

**Use Case:** Reusable email/string utilities, helper functions across modules

---

### `test.py` - Testing Utility Functions

**Purpose:** Tests functionality of utility functions from `utils.py`.

**Concepts:**
- Module importing
- Function testing
- Output validation

**Code Example:**
```python
from utils import username_extracter

print(username_extracter('arjun@example.com'))
```

**Output:** `arjun`

**Testing Approach:**
- Imports specific function from utils module
- Runs the function with sample input
- Verifies output is correct

---

## Data & Utilities

### `employee_data.csv`

Sample employee dataset with columns:
- NAMES: Employee name
- AGE: Age
- CITY: City of residence
- SALARY: Salary amount
- age_group: Categorized age (Young/Adult)
- salary_bonus: Calculated bonus (10% of salary)
- DEPARTMENT: Department (IT/SALES/FINANCE)

**Sample Data:**
```
vishwas,25,Bangalore,25000.0,Adult,2500.0,IT
arjun,21,mumbai,45000.0,Young,4500.0,SALES
```

**Use Cases:**
- Employee data analysis
- Salary calculations
- Department filtering
- CSV processing demonstrations

---

## Jupyter Notebooks

This repository includes several Jupyter notebooks for data analysis and machine learning:

### Data Processing & Visualization
- **`demo_pandas.ipynb`**: Introduction to pandas DataFrame operations
- **`demo_pandas1.ipynb`**: Advanced pandas operations and matplotlib visualization
- **`demo_pandas2.ipynb`**: Data cleaning with pandas (handling missing values)

### Statistical Analysis
- **`Statistics_basics_demo.ipynb`**: Mean, median, mode, variance, standard deviation, covariance, correlation

### Machine Learning
- **`demo_LinearRegression.ipynb`**: Linear regression theory and implementation
- **`Logistic_Regression.ipynb`**: Classification using logistic regression
- **`demo_email_classifier.ipynb`**: Email spam classification with TF-IDF and logistic regression

### Domain-Specific Analysis
- **`Q2-Student_performance_EDA.ipynb`**: Exploratory Data Analysis on student performance
- **`house_prices_scratchpad.ipynb`**: House rental price prediction

### Database Operations
- **`demo_mongo.ipynb`**: MongoDB connection and data retrieval
- **`demo_mysql.ipynb`**: MySQL database operations with SQLAlchemy

---

## Key Python Concepts Summary

| Concept | Files | Description |
|---------|-------|-------------|
| **Variables & Operators** | `first.py` | Basic data types and arithmetic |
| **Control Flow** | `third.py` | Loops and conditionals |
| **Functions** | `utils.py`, `test.py` | Function definition and calling |
| **OOP Basics** | `second.py` | Classes and inheritance |
| **Encapsulation** | `demo_access.py` | Private attributes and properties |
| **Decorators** | `demo_decorators.py` | Function/method wrappers |
| **Comprehensions** | `demo_comprehensions.py` | List/dict creation shortcuts |
| **Functional Programming** | `demo_fp.py` | Pure functions and immutability |
| **File I/O** | `demo_files.py` | Reading/writing files safely |
| **CSV Processing** | `demo_csv.py` | Structured data handling |
| **Data Validation** | `demo_dataclasses.py` | Type checking with Pydantic |

---

## Running the Files

### Execute a Python Script
```bash
python first.py
python demo_csv.py
python test.py
```

### Run Jupyter Notebooks
```bash
jupyter notebook demo_pandas.ipynb
```

### Interactive Testing
```bash
python -i utils.py
>>> username_extracter('test@example.com')
'test'
```

---

## Best Practices Demonstrated

1. **Exception Handling**: Use `try-except` for error management
2. **Resource Management**: Use `with` statement for file operations
3. **Documentation**: Write docstrings for functions
4. **Code Organization**: Group related code in modules and classes
5. **Immutability**: Favor pure functions over side effects
6. **Type Hints**: Use type annotations for clarity
7. **Testing**: Separate test code in test files
8. **Naming**: Use descriptive names for variables and functions

---

## Dependencies

- **Standard Library**: `csv`, `datetime`, `sqlite3`
- **Third-Party**: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `pydantic`, `pymongo`, `sqlalchemy`

---

## Notes

- Some files have commented-out code showing alternative implementations
- The `third.py` file contains a logical bug for educational purposes (total accumulation)
- Use notebooks for data analysis; use scripts for production code
- Follow PEP 8 style guidelines for Python code

---

**Last Updated:** February 2026
