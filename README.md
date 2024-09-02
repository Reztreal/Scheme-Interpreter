# Scheme Interpreter

This project is an implementation of an interpreter for a subset of the Scheme programming language. Scheme is a minimalist dialect of Lisp, known for its simple syntax and powerful features. This interpreter evaluates Scheme expressions, including arithmetic operations, variable definitions, user-defined procedures, and special forms.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Examples](#examples)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This interpreter was built to understand the principles of programming language design and implementation. It covers the basic aspects of functional programming as used in Scheme and helps explore how interpreters parse and evaluate code. The interpreter is designed to handle a subset of Scheme features, focusing on fundamental operations, user-defined functions, and special forms.

## Features

- **Basic Data Types**: The interpreter supports fundamental Scheme data types such as numbers, booleans, symbols, and lists. 
  - Numbers: Both integers and floating-point numbers are supported.
  - Booleans: Scheme uses `#t` for true and `#f` for false.
  - Symbols: Arbitrary names that can be bound to values.
  - Lists: Constructed using the `cons` function and can be manipulated using standard list operations.

- **Arithmetic Operations**: Built-in support for common arithmetic operations.
  - `+`, `-`, `*`, `/`: Supports addition, subtraction, multiplication, and division.
  - Supports variadic arguments, allowing operations on multiple numbers at once.
  - Nested arithmetic expressions are evaluated according to standard precedence rules.
  
  ```scheme
  scm> (+ 1 2 3)      ; Adds 1, 2, and 3
  6
  scm> (* 2 3 4)      ; Multiplies 2, 3, and 4
  24
  ```

- **Variable Definitions**: Use the `define` keyword to bind names to values, allowing for variable storage and reuse.
  - Supports binding symbols to numbers, booleans, strings, lists, and functions.
  - Once defined, variables can be referenced in subsequent expressions.

  ```scheme
  scm> (define x 10)  ; Defines x and binds it to 10
  x
  scm> x
  10
  ```

- **Conditional Expressions**: Evaluate expressions based on conditions using the `if` special form.
  - `if` takes three arguments: a condition, a consequent (executed if the condition is true), and an alternative (executed if the condition is false).
  - Only the branch corresponding to a true condition is evaluated.

  ```scheme
  scm> (if (> 10 5) 'yes 'no)  ; Checks if 10 is greater than 5
  yes
  ```

- **Function Definitions**: Create reusable functions using the `lambda` special form or shorthand `define` syntax.
  - `lambda` creates anonymous functions with specified parameters and body expressions.
  - Named functions can be created using the shorthand syntax `(define (name params) body)`.
  - Supports functions with multiple arguments and nested expressions.

  ```scheme
  scm> (define (square x) (* x x))  ; Defines a function to square a number
  square
  scm> (square 5)                   ; Calls the square function with 5
  25
  ```

- **Special Forms**: The interpreter supports various special forms that alter the evaluation order or scope.
  - **`let`**: Allows creating local bindings within a block, useful for temporary variables and complex calculations.
    ```scheme
    scm> (let ((x 42) (y (* x 10))) (list x y))  ; Local x, y bindings
    (42 420)
    ```
  - **`and`** / **`or`**: Logical operations that short-circuit, stopping evaluation as soon as the result is determined.
    ```scheme
    scm> (and 1 2 #f)  ; Evaluates until it finds #f
    #f
    scm> (or #f 3 4)   ; Evaluates until it finds a true value
    3
    ```
  - **`cond`**: A multi-way conditional that evaluates multiple conditions sequentially until one is true.
    ```scheme
    scm> (cond ((> 4 5) 'no) ((< 4 5) 'yes) (else 'maybe))
    yes
    ```

- **Error Handling**: The interpreter includes basic error handling to catch and report common errors:
  - Undefined variables.
  - Incorrect argument counts in function calls.
  - Invalid operations (e.g., division by zero).
  - Duplicate variable definitions in a single scope.
  - These errors help maintain robustness and guide the user towards correct usage.

## Getting Started

### Prerequisites

To run the Scheme interpreter, you will need:

- **Python 3.x**: The interpreter is written in Python, so ensure you have Python 3 installed on your system.

### Installation

1. **Clone the Repository**:

   Clone the repository to your local machine using:

   ```bash
   git clone https://github.com/your-username/scheme-interpreter.git
   cd scheme-interpreter
   ```

2. **Run the Interpreter**:

   Start the interpreter by running:

   ```bash
   python3 scheme.py
   ```

   This will start a REPL (Read-Eval-Print Loop), where you can enter Scheme expressions and see their results.

## Usage

Once the interpreter is running, you can interact with it by typing Scheme expressions at the prompt.

### Defining Variables

Define a variable using the `define` keyword:

```scheme
scm> (define x 10)
x
scm> x
10
```

### Arithmetic Operations

Perform arithmetic operations using standard operators:

```scheme
scm> (+ 1 2 3)
6
scm> (* 2 3 4)
24
```

### Conditional Expressions

Use `if` for conditional logic:

```scheme
scm> (if (> 10 5) 'yes 'no)
yes
```

### Defining Functions

Define functions using `lambda` or shorthand `define`:

```scheme
scm> (define (square x) (* x x))
square
scm> (square 5)
25
```

### Using `let` for Local Bindings

The `let` form allows you to bind variables locally:

```scheme
scm> (let ((x 42) (y (* x 10))) (list x y))
(42 420)
```

## Examples

Here are a few examples of how to use the interpreter:

1. **Basic Arithmetic**:
    ```scheme
    scm> (+ 3 4)
    7
    scm> (- 10 3)
    7
    scm> (* 2 3 4)
    24
    ```

2. **Defining and Using Variables**:
    ```scheme
    scm> (define a 5)
    a
    scm> (define b (* a 2))
    b
    scm> b
    10
    ```

3. **Creating and Using Functions**:
    ```scheme
    scm> (define (add-two x) (+ x 2))
    add-two
    scm> (add-two 5)
    7
    ```

4. **Using Special Forms**:
    ```scheme
    scm> (define x 10)
    x
    scm> (let ((x 5) (y 10)) (+ x y))
    15
    scm> x
    10  ; x is still 10, demonstrating local binding in let
    ```

## How It Works

### Evaluation Model

The interpreter uses a typical "read-eval-print" cycle:

1. **Read**: Parses input Scheme expressions.
2. **Eval**: Evaluates the expressions in a given environment.
3. **Print**: Outputs the result of evaluation.

### Environments and Frames

- The interpreter maintains an environment, a mapping of symbols to values, to keep track of variable bindings.
- It supports creating new environments using frames, which can have parent frames, allowing for nested scopes.

### Special Forms

Special forms are expressions that have special evaluation rules. The interpreter supports special forms like `define`, `lambda`, `if`, `let`, and more, each implemented with specific handling logic.

### Error Handling

The interpreter includes error handling to catch common mistakes, such as using undefined variables, incorrect argument counts, and invalid forms.
