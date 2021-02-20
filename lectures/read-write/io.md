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
- Command Line Input
- Handling Special File Types

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

To read a file it must exist.

```python
with open("missing.txt") as f:
    pass
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
```
<!-- .element: class="fragment" -->

--

## Writing Files

Writing also makes use of a *context*.

--

## Example

```python
with open("out.txt", "w") as f:
    f.write("a line to write\n")
```

The second argument to `open` is the file *mode*.
<!-- .element: class="fragment" -->

--

# Warning

*if you open an existing file in write mode...*

**it will erase any contents without warning**
<!-- .element: class="fragment" -->

--

## File modes

- `"r"` read from a file (default)
- `"w"` writes to a file
- `"a"` opens the file for appending
- `"x"` create a file - error if it already exists
- `"r+"` opens the file for both reading and writing

--

## Text or Binary

- `"t"` Text - human readable (Default)
- `"b"` Binary mode

Note: In most cases - read and write text files. Binary files
need a good specification to ensure future compatibility.

--

## Methods of File Objects

There are more options aside from `read()` and `write()`.

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

This is memory *efficient* and *fast*.
<!-- .element: class="fragment" -->

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

--

## Finer Control

--

This is our test file

```text
A short text file
with
more than
one
line
```

--

## Line by Line

```python [1 | 2 | 3 | 4 | 5 | 6 | 7]
with open("test.txt") as f:
    while True:
        chunk = f.read(3)
        if not chunk:
            print("<end of file>")
            break
        print(chunk, end="*")
```

--

```python 
with open("test.txt") as f:
    while True:
        chunk = f.read(3)
        if not chunk:
            print("<end of file>")
            break
        print(chunk, end="*")
```

```text
A s*hor*t t*ext* fi*le
*wit*h
m*ore* th*an
*one*
li*ne
*<end of file>
```
<!-- .element: class="fragment" -->

---

# User Input

--

```python
while True:
    value = input("Enter a value, or type 'q' to quit: ")
    if value == "q":
        print("Quitting...")
        break
    print("You entered: ", value)
```

```text
$: python inputs.py 
```
<!-- .element: class="fragment" -->


--

```text [1|2|3|4|5|6|7|8]
Enter a value, or type 'q' to quit: a
You entered:  a
Enter a value, or type 'q' to quit: b
You entered:  b
Enter a value, or type 'q' to quit: c
You entered:  c
Enter a value, or type 'q' to quit: q
Quitting...
```

--

## FYI

`input()` works in a **Jupyter Notebook**

---

## Command Line Arguments

---

# Special File Types

---