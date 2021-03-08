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

Notes: https://docs.python.org/3/howto/logging.html#when-to-use-logging

--

<!-- .slide: data-auto-animate -->
## Logging

* Send logs to multiple outputs.
<!-- .element: class="fragment" -->
* Segregate logging according to module structure
<!-- .element: class="fragment" -->
* Define logging at different levels
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


--

https://docs.python.org/3/howto/logging-cookbook.html

An excellent advanced tutorial on logging, including multi threading.

--
