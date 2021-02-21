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

`test.txt`

```text
A short text file
with
more than
one
line
```

--

## Contexts

Python has a useful construct: the **context manager**

A context helps us open files safely with minimal code.
<!-- .element: class="fragment" -->

We create a context using the keyword `with`
<!-- .element: class="fragment" -->

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
more than
one
line
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

## Case Study

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

# Command Line Interface (CLI)

--

A CLI is enabled by the *shell* interpreter. 

The shell exposes a command prompt.

Windows: `PowerShell`
<!-- .element: class="fragment" -->

Unix: `bash`, `zsh`, etc...
<!-- .element: class="fragment" -->

--

CLI has:

- A **command** or program 
- Zero or more command line **arguments** 

--

### Python Command Line

```text
$ python -h
```

- `python` is the command
- `-h` is an argument - in this case *optional*

**Do** try this at home
<!-- .element: class="fragment" -->

--

### `script.py`

```python [1 | 3 | 4 | 5 | 6 | 8]
import sys

def main():
    print("Printing Args:")
    for i, arg in enumerate(sys.argv):
        print(f"Arg {i} is: '{arg}'")

main()

```

--

```python
import sys

def main():
    print("Printing Args:")
    for i, arg in enumerate(sys.argv):
        print(f"Arg {i} is: '{arg}'")

main()

```

--

### In the shell - example 1

```python
$ python script.py
```

```text
Printing Args:
Arg 0 is: 'script.py'
```
<!-- .element: class="fragment" -->


- `python` is the command
- `script.py` is an argument

<!-- .element: class="fragment" -->

--

### In the shell - example 2

```python
$ python script.py value another "yet another"
```

```text
Printing Args:
Arg 0 is: 'script.py'
Arg 1 is: 'value'
Arg 2 is: 'another'
Arg 3 is: 'yet another'
```
<!-- .element: class="fragment" -->

- `python` is the command
- `script.py value another "yet another"`  are arguments

<!-- .element: class="fragment" -->

--

## `argparse`

https://docs.python.org/3/library/argparse.html

Note: If you want to go beyond the simplest case, consider argparse.

--

## `prog.py`

```python
import argparse

parser = argparse.ArgumentParser(
    description='Process some integers.')
parser.add_argument(
    'integers', metavar='N', type=int, nargs='+',
    help='an integer for the accumulator')
parser.add_argument(
    '--sum', dest='accumulate', action='store_const',
    const=sum, default=max,
    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

--

```text
$ python prog.py -h
```

```text
usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
  N           an integer for the accumulator

optional arguments:
  -h, --help  show this help message and exit
  --sum       sum the integers (default: find the max)
```
<!-- .element: class="fragment" -->

--

## Third party parsers

**click**

https://palletsprojects.com/p/click/


---

# Special File Types

--

## JSON 
### JavaScript Object Notation

https://docs.python.org/3/library/json.html

--

JSON exists as a `string`

```python
s = '{"name": "red", "values": [255, 0, 0]}'
```

Note: This format follows the dictionary literal from last week.

--

```python
import json

s = '{"name": "red", "values": [255, 0, 0]}'
col = json.loads(s)
```

`col` is a `dictionary`
<!-- .element: class="fragment" -->

```python
print(col["name"])
```
<!-- .element: class="fragment" -->

```text
red
```
<!-- .element: class="fragment" -->

--

convert a `dictionary` to a JSON `string`

```python
import json

col = dict(name="red", values=[255, 0, 0])
s = json.dumps(col)

print(s)
```

```text
{"name": "red", "values": [255, 0, 0]}
```
<!-- .element: class="fragment" -->

--

### FYI

The JSON format only supports basic `types`

User defined classes, numpy arrays, etc. are not supported.

--

## Reading from file

```python
import json

with open("colours.json") as f:
    cold = json.load(f)
```

The `json.load()` method accepts a  `file`  object.
<!-- .element: class="fragment" -->

`cold` is a `dictionary`
<!-- .element: class="fragment" -->

Note: very similar to earlier examples...

--

### Formatting

The `json.dumps()` method has a formatting option.

```python
import json

with open("colours.json") as f:
    cold = json.load(f)

cols = json.dumps(cold, indent=4)
print(cols)
```

--

```text
{
    "colors": [
        {
            "name": "red",
            "values": [
                255,
                0,
                0
            ]
        },
        {
            "name": "green",
            "values": [
...
```

Note: the output is truncated on the slide

--

## Writing JSON

```python
import json

col = dict(name="red", values=[255, 0, 0])

with open("red.json", "w") as f:
    json.dump(col, f)
```

--

### Formatting

The `json.dump()` method also has a formatting option.

---

# Questions

---

Slides and code are available on Teams

I have also made everything available on GitHub

https://github.com/uea-teaching/python-introduction
