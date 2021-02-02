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
<!-- .element: class="fragment" data-fragment-index="1" -->

---

## Why do we need functions?

Functions allow us to organise code in a logical way.
<!-- .element: class="fragment" data-fragment-index="1" -->

Functions allow us to avoid repeating code.
<!-- .element: class="fragment" data-fragment-index="2" -->

---

<h1 style="color:#ff00ff">DRY</h1>

## Don't Repeat Yourself
<!-- .element: class="fragment" data-fragment-index="1" -->

---

## Python has around 70 built-in functions

https://docs.python.org/3/library/functions.html


---

## You will use this one more than any other

```python
print("hello world!")
```
<!-- .element: class="fragment" data-fragment-index="2" -->

```repl
>>> hello world!
```
<!-- .element: class="fragment" data-fragment-index="3" -->

---

# Define a function

---

A function is defined using the `def` keyword.

```python
def my_function():
  print("Hello from a function")
```
<!-- .element: class="fragment" data-fragment-index="2" -->

---

```python
def add_two(a, b):
    """Add two numbers and return the sum."""
    return a + b
```

---

```python [1|2|3]
def add_two(a, b):
    """Add two numbers and return the sum."""
    return a + b
```

---


---
