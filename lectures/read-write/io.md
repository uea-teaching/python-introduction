# input and output
### With Python

Dr. David Greenwood

david.greenwood@uea.ac.uk

Room SCI 2.16a

---

## Resources

- https://docs.python.org/ 

- https://www.w3schools.com/python/


Note: Take care with online resources, that they are up to date and accurate

---

## Contents

- Reading and writing files
- Reading and writing to streams
- Handling large files

---

## Motivation

Computer programs rarely exist in isolation.

We usually need to consider reading and writing data or accepting user input.

---

## Reading Files

We use the built-in `open()` function to read files in Python.

--

## Contexts

Python has a useful construct, the context manager, that helps us open files safely with minimal code.

We create a context using the keyword `with`

--

## Example

```python
with open("test.txt") as f:
    data = f.read()

print(data)
```

```text
'A short text file\nwith\nmore than\none\nline\n'
```
<!-- .element: class="fragment" -->

--

### without using a context

```python
try:
    f = open('test.txt')
except Exception:
    raise 
finally:
    f.close()
```

### <span class="bright"> Don't do it! </span>
<!-- .element: class="fragment" -->

--

Our example reads a plain text file.
The data is returned as a `string`.

Note: there are other file types than text...

--

## Writing Files

Writing also makes use of a <span class="bright">
context</span>.

--

## Example

```python
with open("out.txt", "w") as f:
    f.write("a line to write\n")
```

The second argument to `open` is the file <span class="bright">
mode</span>.
<!-- .element: class="fragment" -->

--

## File modes

- `r` read from a file
- `w` writes to a file
- `a` opens the file for appending
- `r+` opens the file for both reading and writing

> consult the python docs for details
<!-- .element: class="fragment" -->

--

## Methods of File Objects

We have more options than `read()` and `write()`.

--

### Example - read one line

```python
with open("test.txt") as f:
    data = f.readline()

print(data)
```

```text
'A short text file\n'
```
<!-- .element: class="fragment" -->

--

### Example - read to list

```python
with open("test.txt") as f:
    data = f.readlines()

print(data)
```

```text
['A short text file\n', 'with\n', 'more than\n', ...]
```
<!-- .element: class="fragment" -->

--

For reading lines from a file, 
you can loop over the file object. 
This is memory efficient and fast.

--

### Example - iterable

```python
with open("test.txt") as f:
    for line in f:
        print(line, end="")
```

```text
A short text file
with
more than ...
```
<!-- .element: class="fragment" -->

---
