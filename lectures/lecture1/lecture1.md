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

Arguments are separated by a comma, inside the parentheses of the function definition.
<!-- .element: class="fragment" -->

---

```python
def times_two(a):
    """print 'a' times 2."""
    print(a * 2)
```

---

```python [1|2|3]
def times_two(a):
    """print 'a' times 2."""
    print(a * 2)
```

---
