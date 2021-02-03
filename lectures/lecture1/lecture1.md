# Functions in Python

Dr. David Greenwood

david.greenwood@uea.ac.uk

Room SCI 2.16a

---

## Resources

- https://docs.python.org/ 

- https://www.w3schools.com/python/

---

## What is a function?

A function is a block of code that only runs when it is called.
<!-- .element: class="fragment" -->

---

## Why do we need functions?

Functions allow us to organise code in a logical way.
<!-- .element: class="fragment" -->

Functions allow us to avoid repeating code.
<!-- .element: class="fragment" -->

---

<h1 style="color:#ff00ff">DRY</h1>

## Don't Repeat Yourself
<!-- .element: class="fragment" -->

---

## Python has around 70 built-in functions

https://docs.python.org/3/library/functions.html


---

## You will use this one more than any other

```python
print("hello world!")
```
<!-- .element: class="fragment" -->

```bash
>>> hello world!
```
<!-- .element: class="fragment"-->

---

# Define a function

---

### A function is defined using the `def` keyword

```python
def my_function():
  print("Hello from a function")
```
<!-- .element: class="fragment" -->

---

#### indentation

Notice the *indentation* inside the function block.
<!-- .element: class="fragment" -->

Indentation is part of the language *syntax*.
<!-- .element: class="fragment" -->

---

## Calling a function

use the function name, followed by parentheses
<!-- .element: class="fragment" -->
```python [1-2|4]
def my_function():
  print("Hello from a function!")

my_function()
```
<!-- .element: class="fragment" -->

---

```c
>>> Hello from a function!
```

---

## values can be passed into functions as arguments

Parameters are separated by a comma, inside the parentheses of the function definition.
<!-- .element: class="fragment" -->

---

This function has one parameter

```python
def times_two(a):
    print(a * 2)
```
<!-- .element: class="fragment" -->

```c
times_two(3)
>>> 6
```
<!-- .element: class="fragment" -->

---

# Parameters or Arguments

A *parameter* is a variable in a function definition. 
When a function is called, the *arguments* are the 
data you pass into the function's parameters.
<!-- .element: class="fragment" -->

---

## Number of Arguments

A function must be called with the correct number of arguments. 
<!-- .element: class="fragment" -->
If your function expects 2 arguments, you have to call the function 
with 2 arguments, not more, and not less.
<!-- .element: class="fragment" -->

---

### Example - wrong number of arguments

```python
def sum_two(a, b):
    print(a + b)
```
<!-- .element: class="fragment" -->

```c
sum_two(3)
```
<!-- .element: class="fragment" -->

```
TypeError: 
  sum_two() missing 1 required positional argument: 'b'
```
<!-- .element: class="fragment" -->

---

### Arbitrary Arguments:
### `*args`

Note:
If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, 
and can access the items accordingly.

---

#### Example

```python [1-3| 5]
def print_numbers(*numbers):
    for number in numbers:
        print(number)

print_numbers(1, 2, 3)
```

---

## Keyword Arguments

You can pass arguments with the `key = value` syntax.
<!-- .element: class="fragment" -->
This way, the order of the arguments does not matter.
<!-- .element: class="fragment" -->

---

#### Example

```python [1-2| 4]
def sum_two(a, b):
    print(a + b)

sum_two(b=3, a=2)
```

---

Keyword Arguments are often termed `kwargs` in Python documents.

---

### Arbitrary Keyword Arguments
### `**kwargs`

Note:
If you do not know how many keyword arguments that will be passed into your 
function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, 
and can access the items accordingly.

---

#### Example

```python [1-5|7]
def sum_three(**kwargs):
    a = kwargs.get("a")
    b = kwargs.get("b")
    c = kwargs.get("c")
    print(a + b + c)

sum_three(c=3, a=1, b=2)
```

---

In this example the function receives a **dictionary** of arguments.

Consult the Python documents to understand the `kwargs.get()` function used here.

---

## Default parameter values

---

#### Example

``` python [1-2|4]
def sum_two(a, b=3):
    print(a + b)

sum_two(3)
```

---

### `*args, **kwargs`

---

#### Example

``` python [1-2|4]
def sum_two_or_more(*args, **kwargs):
    print(args[0] + args[1] + kwargs.get("c"))

sum_two_or_more(3, 2, c=4)
```

---

### What doesn't work

``` python [1-2|4]
def will_break(a, b=3, c):
    print(a+b+c)

will_break(1, 2, 3)
```

```python
SyntaxError: non-default argument follows default argument
```
<!-- .element: class="fragment" -->

---

### What doesn't work

``` python [1-2|4]
def sum_two(a, b):
    print(a + b)

sum_two(a=2, b)
```

```python
SyntaxError: positional argument follows keyword argument
```
<!-- .element: class="fragment" -->

---

The Python interpreter first consumes all positional arguments, then any keyword arguments.

---

### Functions can't be empty

---

During development, you might want to write function definitions before fully implementing the code.

```python [1-2|4]
def dev_function():
  pass

dev_function()
```
<!-- .element: class="fragment" -->


---

# Return Values

To let a function return a value, use the return statement

---

