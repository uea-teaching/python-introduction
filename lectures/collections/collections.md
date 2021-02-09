# Python Collections

Dr. David Greenwood

david.greenwood@uea.ac.uk

Room SCI 2.16a

---

## Resources

- https://docs.python.org/ 

- https://www.w3schools.com/python/

---

## Contents

- Tuples, Lists, Sets and Dictionaries
- Reading from and writing to collections
- Methods on collections

---

# Tuple

A tuple is a collection which is 
<span style="color:coral">**ordered**</span> and
<span style="color:coral">**immutable**</span>.
<!-- .element: class="fragment" -->

--

![pronouncing](../assets/tuhple-toople.jpg)

--

Tuples are used to store multiple items in a single variable.

Tuples are written with parentheses (round brackets).
<!-- .element: class="fragment" -->

--

```python
mytuple = ("apple", "banana", "cherry")
```

--

Tuple items are ordered, unchangeable, and allow duplicate values

--

As tuples are ordered, we access items by indexing
<!-- .element: class="fragment" -->

```python
mytuple[0]
```
<!-- .element: class="fragment" -->

```text
apple
```
<!-- .element: class="fragment" -->

Note:
We will dive deeper into indexing with `lists`

--

Because tuples are immutable, we can't change items.

```python [1 | 3]
fruits = ("apple", "banana", "cherry")

fruits[0] = "orange"
```

```text
TypeError: 'tuple' object does not support item assignment
```
<!-- .element: class="fragment" -->

--

Tuples can have multiple items with the same value.

```python
fruit = ("apple", "banana", "cherry", "apple", "banana")
```
<!-- .element: class="fragment" -->

--

To determine how many items a tuple has, use the `len()` function

```python
fruits = ("apple", "banana", "cherry")
print(len(fruits))
```
<!-- .element: class="fragment" -->

--

For a tuple with only one item, you must use a trailing comma.

```python
fruits = ("apple",)
```
<!-- .element: class="fragment" -->

--

# Why?

Without the comma, Python treats the contents of parentheses as an expression
<!-- .element: class="fragment" -->

--

## Data types

Tuple items can be of any data type.
<!-- .element: class="fragment" -->

--

```python
fruits = ("apple", "banana", "cherry")
numbs = (1, 5, 7, 9, 3)
dares = (True, False, False)
```

--

Tuple items can be of mixed data type.

```python
mixed = ("apple", 1, True, False)
```
<!-- .element: class="fragment" -->

---

# Questions

---

Slides and code are available on BlackBoard

I have also made them available on GitHub

https://github.com/uea-teaching/python-introduction
