# Python Collections

Dr. David Greenwood

david.greenwood@uea.ac.uk

Room SCI 2.16a

---

## Resources

- https://docs.python.org/ 

- https://www.w3schools.com/python/


Note: Take care with online resources, that they are uo to date and accurate

---

## Contents

- Tuples, Lists, Sets and Dictionaries
- Reading from and writing to collections
- Comprehensions
- Methods on collections

---

# Tuples

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
fruits = ("apple", "banana", "cherry")
```

--

Tuple items are ordered, unchangeable, and allow duplicate values

--

As tuples are ordered, we access items by indexing

```python
print(fruits[0])
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
fruits = ("apple", "banana", "cherry", "apple", "banana")
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
numbers = (1, 5, 7, 9, 3)
answers = (True, False, False)
```

--

Tuple items can be of mixed data type.

```python
mixed_types = ("apple", 1, True)
```
<!-- .element: class="fragment" -->

--

## Tuple unpacking

extract tuple items back into variables
<!-- .element: class="fragment" -->

--

```python [1 | 2]
fruits = ("apple", "banana", "cherry")
a, b, c = fruits
```

--

```python
print(a)
```

```text
apple
```
<!-- .element: class="fragment" -->

--

## FYI

When a function returns multiple values, it returns a tuple. 

---

# Lists

A list is a collection which is 
<span style="color:coral">**ordered**</span> and
<span style="color:coral">**mutable**</span>.
<!-- .element: class="fragment" -->

--

Lists are used to store multiple items in a single variable.

Lists are written with [ square ] brackets .
<!-- .element: class="fragment" -->

--

```python
fruits = ["apple", "banana", "cherry"]
```

--

### lists are ordered

we access items by indexing

```python
print(fruits[0])
```
<!-- .element: class="fragment" -->

```text
apple
```
<!-- .element: class="fragment" -->

--

### lists *are* mutable 
### we *can* change items

```python [1 | 3]
fruits = ["apple", "banana", "cherry"]

fruits[0] = "orange"
```

```python [1 | 3]
print(fruits)

['orange', 'banana', 'cherry']
```
<!-- .element: class="fragment" -->

--

## Data types

List items can be of any data type.
<!-- .element: class="fragment" -->

--

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 5, 7, 9, 3]
answers = [True, False, False]
```

--

List items can be of mixed data type.

```python
mixed_types = ["apple", 1, True]
```
<!-- .element: class="fragment" -->

---

# Indexing

--

## Reminder

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```

```text
banana
```
<!-- .element: class="fragment" -->

Note: Why is it banana?

--

### Errors

```python
letters = ["a", "b", "c"]
print(letters[3])
```

```text
IndexError: list index out of range
```
<!-- .element: class="fragment" -->

--

### Negative Indexing

We can index from the end of the list!

-1 is the last item, -2 is next to last item...
<!-- .element: class="fragment" -->

--

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
```

```text
cherry
```
<!-- .element: class="fragment" -->

--

### Range of Indices

The `:` operator allows a `range` of indices.

Note: You can specify a range of indexes by specifying 
where to start and where to end the range.

--

```python
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters[2:5])
```

```text
['c', 'd', 'e']
```
<!-- .element: class="fragment" -->

--

### defaults

- default start is 0
- default end is `len()` of collection
- default interval (step) is 1
- range is start to end -1

--

#### example 

```python
letters = ["a", "b", "c"]
print(letters[:2])
```

```text
['a', 'b']
```
<!-- .element: class="fragment" -->

--

#### example 

```python
letters = ["a", "b", "c"]
print(letters[1:])
```

```text
['b', 'c']
```
<!-- .element: class="fragment" -->

--

#### example 

```python
letters = ["a", "b", "c"]
print(letters[::-1])
```

```text
['c', 'b', 'a']
```
<!-- .element: class="fragment" -->

---

# Iterables

Python collections are <span style="color:coral">`iterable`</span> 

We can use a <span style="color:coral">`for`</span> loop
<!-- .element: class="fragment" -->

---

# Comprehensions

---

# Questions

---

Slides and code are available on BlackBoard

I have also made them available on GitHub

https://github.com/uea-teaching/python-introduction
