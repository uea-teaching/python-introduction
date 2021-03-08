# Logging Testing Debugging
### IN PYTHON

Dr. David Greenwood

david.greenwood@uea.ac.uk

Room SCI 2.16a

--

## Resources

- https://docs.python.org/ 

- https://www.w3schools.com/python/


Note: Take care with online resources, that they are up to date and accurate

--

## Contents

- Logging
- Testing
- Debugging

--

## Motivation

As computer programs get more complex, problems are more likely to appear.

Keeping logs, unit testing and debugging are the tools we have to manage these problems.

Note: https://12factor.net

---

<!-- .slide: data-auto-animate -->
## Logging

--

<!-- .slide: data-auto-animate -->
## Logging

The simplest way to report the status of a program is the `print()` statement. 

--

<!-- .slide: data-auto-animate -->
## Logging

The `logging` module greatly extends this facility

Note: https://docs.python.org/3/howto/logging.html#when-to-use-logging

--

<!-- .slide: data-auto-animate -->
## Logging

Writing logs is a big topic, more info here:

* [Basic Tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
* [Advanced Tutorial](https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial)
* [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)

--

<!-- .slide: data-auto-animate -->
## Logging

What can we do?

* send logs to multiple outputs
<!-- .element: class="fragment" -->
* segregate logging according to module structure
<!-- .element: class="fragment" -->
* define logging at different levels
<!-- .element: class="fragment" -->

Note: stdout, stderr, and files...

--

<!-- .slide: data-auto-animate -->
## Logging

The logging module has builtin functions named for the severity of events.

`DEBUG INFO WARNING ERROR CRITICAL`
<!-- .element: class="fragment" -->

Note:
DEBUG Detailed information, typically of interest only when diagnosing problems.

INFO Confirmation that things are working as expected.

WARNING An indication that something unexpected happened, 
or indicative of some problem in the near future . 
The software is still working as expected.

ERROR Due to a more serious problem, the software has not been able to perform some function.

CRITICAL A serious error, indicating that the program itself may be unable to continue running.

--

Default level is `WARNING`

Only this level - or more severe - will be reported by default.

--

Logging Level

```python
import logging
logging.warning("This is a warning")
logging.info("This is info, it will not show by default!")
```

```text
WARNING:root:This is a warning
```
<!-- .element: class="fragment" -->

Note: log1.py

--

Logging to Files

```python
import logging
logging.basicConfig(
    level=logging.INFO, filename="example.log")

logging.debug("This message will not go to the log file")
logging.info("This will go to the log file.")
logging.warning("And this, too")
logging.error("That's torn it!!")
```

```text
INFO:root:This will go to the log file.
WARNING:root:And this, too
ERROR:root:That's torn it!!
```
<!-- .element: class="fragment" -->

Note: log2.py, example.log

--

### `logging.basicConfig(...)`

As the name suggests, we can configure our logs here.
<!-- .element: class="fragment" -->

The call to `basicConfig()` should come before any calls to `debug()`, `info()` etc.

<!-- .element: class="fragment" -->

Note: In the previous example I used basicConfig()...
I wont look at every option - don't forget the help!

--

### Formatter
<!-- .slide: data-auto-animate -->


Formatter objects configure the final order, structure, and contents of the log message.

--

### Formatter
<!-- .slide: data-auto-animate -->


```python
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
```

Note: This creates a formatter object. 

--

### Formatter
<!-- .slide: data-auto-animate -->

In most cases it easier to pass a string to `basicConfig()`

--

### Formatter
<!-- .slide: data-auto-animate -->

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")
```

--

### Formatter
<!-- .slide: data-auto-animate -->

Using default output to `stderr`

```text
2021-03-08 12:51:00,391 - INFO - This will go to the log file.
2021-03-08 12:51:00,391 - WARNING - And this, too
2021-03-08 12:51:00,391 - ERROR - That's torn it!!
```

Note: Formatting is in itself a large subject. 
There is extensive documentation.

--

### Handlers
<!-- .slide: data-auto-animate -->

Handler objects despatch log messages to the specified destination.

--


### Handlers
<!-- .slide: data-auto-animate -->

```python
handler = logging.StreamHandler()
```

Note: This creates a handler object.

--

### Handlers
<!-- .slide: data-auto-animate -->

We can create handlers for streams and files.

Note: We can add fine grained control such as different levels for each handler. Different threads, modules, etc...

--

### Handlers
<!-- .slide: data-auto-animate -->

We will use `basicConfig()` to set up some handlers.

Note: https://stackoverflow.com/a/46098711/10188737

--

### Handlers
<!-- .slide: data-auto-animate -->

```python
filehandler = logging.FileHandler("debug.log")
filehandler.setLevel(logging.DEBUG)

streamhandler = logging.StreamHandler()
streamhandler.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[filehandler, streamhandler]
)
```

--

### Handlers
<!-- .slide: data-auto-animate -->

```python
logging.debug("This will go to the debug log file")
logging.info("See the debug log file and std err.")
logging.warning("And this, too")
```

```text
2021-03-08 14:43:07 [DEBUG] This will go to the debug log file
2021-03-08 14:43:07 [INFO] See the debug log file and std err.
2021-03-08 14:43:07 [WARNING] And this, too
```

--

### Handlers
<!-- .slide: data-auto-animate -->

```python [4]
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[filehandler, streamhandler]
)
```

Notice the `datefmt` argument!

--

### Naming Loggers
<!-- .slide: data-auto-animate -->

Loggers exist in a hierarchy.

It is useful to know where the message comes from.

--

### Naming Loggers
<!-- .slide: data-auto-animate -->

`aux_mod.py`

```python [1 | ]
LOG = logging.getLogger(__name__)

def some_function():
    LOG.info("calling: 'some_function'")
```

--

### Naming Loggers
<!-- .slide: data-auto-animate -->

`main.py`

```python [7 | ]
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")

logging.info("calling from main: root logger")
some_function()
```

--

### Naming Loggers
<!-- .slide: data-auto-animate -->

```text
2021-03-08 15:05:51 - root - calling from main: root logger
2021-03-08 15:05:51 - log_aux - calling: 'some_function'
```

---

## Unit Testing
<!-- .slide: data-auto-animate -->

--

## Unit Testing
<!-- .slide: data-auto-animate -->

Unit testing is another **big** topic.

Here, I just want to introduce the builtin `unittest` module.
<!-- .element: class="fragment" -->

--

## Unit Testing
<!-- .slide: data-auto-animate -->

Involves developing a *test case* that confirms an assertion.

--

## `Unittest`

* testing framework
* test runner

Note:
unittest contains both a testing framework and a test runner. 
unittest has some important requirements for writing and executing tests.

--

## `Unittest`

* tests are class methods
* assertion methods *not* `assert` statement

Note:
You put your tests into classes as methods
You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement

--

<!-- .slide: data-auto-animate -->
`test_basic.py`

```python
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())

    def test_split(self):
        s = 'hello world'
        with self.assertRaises(TypeError):
            s.split(2)
```

--

<!-- .slide: data-auto-animate -->
`test_basic.py`

```python
if __name__ == '__main__':
    unittest.main()
```

```text
python test_basic.py
```
<!-- .element: class="fragment" -->

```text
...
-------------------------------------
Ran 3 tests in 0.000s

OK
```
<!-- .element: class="fragment" -->

--

<!-- .slide: data-auto-animate -->
### Command Line Interface

```text
python -m unittest -v test_basic.py 
```

`-m` option because `unittest` is a module
<!-- .element: class="fragment" -->

--

<!-- .slide: data-auto-animate -->
### Command Line Interface

`-v` option for verbose output

```text
test_isupper (examples.test_basic.TestStringMethods) ... ok
test_split (examples.test_basic.TestStringMethods) ... ok
test_upper (examples.test_basic.TestStringMethods) ... ok
```
<!-- .element: class="fragment" -->

--

## `Unittest`

`unittest` supports [test discovery](https://docs.python.org/3/library/unittest.html#test-discovery)


--

Many editors support testing frameworks.

Note: VSCode

--

Third Party Test Frameworks

`pytest` 
<!-- .element: class="fragment" -->
`nose`
<!-- .element: class="fragment" -->

...and many [others](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)
<!-- .element: class="fragment" -->

---

## Debugging
