# Functions in Python

Dr. David Greenwood

david.greenwood@uea.ac.uk

Room SCI 2.16a

---

## Resources

- https://docs.python.org/ 

- https://www.w3schools.com/python/

---

## Contents

- Defining functions
- Passing and returning values
- Advanced functions

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

--

<h1 style="color:#ff00ff">DRY</h1>

## Don't Repeat Yourself
<!-- .element: class="fragment" -->

--

## Python has around 70 built-in functions

https://docs.python.org/3/library/functions.html


--

## You will use this one more than any other

```python
print("hello world!")
```
<!-- .element: class="fragment" -->

```text
hello world!
```
<!-- .element: class="fragment"-->

---

# Define a function

--

### A function is defined using the `def` keyword

```python
def my_function():
  print("Hello from a function")
```
<!-- .element: class="fragment" -->

--

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

--

```text
Hello from a function!
```

---

## values can be passed into functions as arguments

Parameters are separated by a comma, inside the parentheses of the function definition.
<!-- .element: class="fragment" -->

--

This function has one parameter

```python
def times_two(a):
    print(a * 2)
```
<!-- .element: class="fragment" -->

```text
times_two(3)

6
```
<!-- .element: class="fragment" -->

--

# Parameters or Arguments

A *parameter* is a variable in a function definition. 
When a function is called, the *arguments* are the 
data you pass into the function's parameters.
<!-- .element: class="fragment" -->

--

## Number of Arguments

A function must be called with the correct number of arguments. 
<!-- .element: class="fragment" -->
If your function expects 2 arguments, you have to call the function 
with 2 arguments, not more, and not less.
<!-- .element: class="fragment" -->

--

#### Example - wrong number of arguments

```python
def sum_two(a, b):
    print(a + b)
```
<!-- .element: class="fragment" -->

```text
sum_two(3)
```
<!-- .element: class="fragment" -->

```text
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

--

#### Example - Arbitrary Arguments

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

--

#### Example - Keyword Arguments

```python [1-2| 4]
def sum_two(a, b):
    print(a + b)

sum_two(b=3, a=2)
```

--

Keyword Arguments are often termed `kwargs` in Python documents.

--

### Arbitrary Keyword Arguments
### `**kwargs`

Note:
If you do not know how many keyword arguments that will be passed into your 
function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, 
and can access the items accordingly.

--

#### Example Arbitrary Kwargs

```python [1-5|7]
def sum_three(**kwargs):
    a = kwargs.get("a")
    b = kwargs.get("b")
    c = kwargs.get("c")
    print(a + b + c)

sum_three(c=3, a=1, b=2)
```

--

In this example the function receives a <span style="color:coral">*dictionary*</span> of arguments.

Consult the Python documents to understand the `kwargs.get()` function used here.

---

## Default parameter values

--

#### Example

``` python [1-2|4]
def sum_two(a, b=3):
    print(a + b)

sum_two(3)
```

---

### `*args, **kwargs`

--

we can combine arbitrary `*args` and `**kwargs`

--

#### Example

``` python [1-2|4]
def sum_two_or_more(*args, **kwargs):
    print(args[0] + args[1] + kwargs.get("c"))

sum_two_or_more(3, 2, c=4)
```

---

## What doesn't work

--

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

--

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

--

The Python interpreter first consumes all positional arguments, then any keyword arguments.

---

### Functions can't be empty

--

During development, you might want to write function definitions before fully implementing the code.

```python [1-2|4]
def dev_function():
  pass

dev_function()
```
<!-- .element: class="fragment" -->

---

# Return Values

--

To let a function return a value, use the `return` statement

--

#### Example - return

```python [1-2|4|5]
def return_sum_two(a, b):
    return a + b

result = return_sum_two(2, b=3)
print(result)
```

---

# Advanced Functions

---

## Lambda Functions

A small anonymous function
<!-- .element: class="fragment" -->
Any number of arguments, but can only have one expression.
<!-- .element: class="fragment" -->

--

## Lambda Function Syntax

```python
lambda arguments : expression
```

The expression is executed and the result is returned

--

#### Example lambda

```python [1 | 3]
func = lambda a : a + 10

print(func(5))
```

--

#### Equivalent to:

```python [1-2 | 4]
def func(a):
    return a + 10

print(func(5))
```

--

## In most cases... 

## you should not use a lambda function! 
<!-- .element: class="fragment" -->

--

## Real World Example 

```python [1 | 2 | 4]
data = [("x", 4), ("y", 1), ("z", -5)]
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)
```

--

```python
[('z', -5), ('y', 1), ('x', 4)]
```

--

This example uses the built in function `sorted`

--

You can print the documentation for a function:

```python
print(sorted.__doc__)
```

--

Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.

--

We supply a custom key function using `lambda`.

```python
sorted_data = sorted(data, key=lambda x: x[1])
```

--

`x[1]`

The `lambda` function returns the second item in each `tuple`

<span style="color:coral">recall:</span> Python indexes from 0
<!-- .element: class="fragment" -->

---

## Doc Strings

--

### What is a doc string?

"A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition"

https://www.python.org/dev/peps/pep-0257/

--

### Example

``` python
def my_function(a, b=5):
    """Return a plus b.
    
    b is optional, and has a default value of 5.
    """
    return a + b
```

We use triple quotes to define the docstring
<!-- .element: class="fragment" -->

--


It is the `__doc__` attribute of the function object.


```python
print(my_function.__doc__)
```
<!-- .element: class="fragment" -->

```text
Return a plus b.
    
    b is optional, and has a default value of 5.
```
<!-- .element: class="fragment" -->

--

### What doesn't work

```python
def my_function(a, b=5):
    # comments do not become docs...
    pass

print(my_function.__doc__)
```

```text
None
```

--

### Always write a docstring!

Many editors show the docstring on hover 
<!-- .element: class="fragment" -->
Really useful as your code gets more complex.
<!-- .element: class="fragment" -->

---

## Nested functions

--

Functions allow us to organise code in a logical way.

--

Nested functions are functions inside an outer function

They can also be called inner functions
<!-- .element: class="fragment" -->

--

#### Example - inner function

```python [1-5|7]
def outer():
  print("I'm the outer function.")
  def inner():
    print("And I'm the inner function.")
  inner()

outer()
```

```text
I'm the outer function.
And I'm the inner function.
```
<!-- .element: class="fragment" -->

--

## The inner function can access data within the scope of the outer function

--

```python [1-5|7]
def outer(s):
  print("I'm the outer function.")
  def inner():
    print("I can see the outer data:", s)
  inner()

outer("this is the outer data")
```

```text
I'm the outer function.
I can see the outer data: this is the outer data
```
<!-- .element: class="fragment" -->

--

Consider carefully if your code design needs nested functions

--

## Closures

- Must have an inner function
<!-- .element: class="fragment" -->
- Nested function refers to a value in outer scope
<!-- .element: class="fragment" -->
- Outer function returns the inner function
<!-- .element: class="fragment" -->

--

#### Example - Closure

```python [1-4|6]
def num1(x):
  def num2(y):
    return x + y
  return num2

print(num1(10)(5))
```

---

## Callbacks

A function can accept a function as an argument.
<!-- .element: class="fragment" -->

--

### Case Study

- You have some buttons in a ui,
- You want to reuse the button function...
- but produce different outcomes.

--

#### Define the functions

```python [1-5|7-9]
def get_square(val):
    return val ** 2

def get_cube(val):
    return val ** 3

def clickme(val, func):
    return func(val)
```

--

#### Call the functions

```python
print(clickme(5, get_square))
```

```text
25
```
<!-- .element: class="fragment" -->

--

#### Call the functions

```python
print(clickme(5, get_cube))
```

```text
125
```
<!-- .element: class="fragment" -->

---

# Questions

---

Slides and code are available on BlackBoard

I have also made them available on GitHub

https://github.com/uea-teaching/python-introduction
