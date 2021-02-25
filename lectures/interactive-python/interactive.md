# Interactive Python

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

- Python Shell
- iPython
- Jupyter

---

## Motivation

Python is a high level general purpose programming language.

It also has an interactive interface, circumventing 
the need to create larger formal coding structures, 
and compiling.

---

# Python Shell

--

The Python shell, or REPL, is the simplest way to access the Language.

However, it is only suitable for the shortest excursions.

--

in your shell, type `python`

![py-shell-start](../assets/img/py-shell-start.png)

--

to get back to your prompt, type `exit()` or `quit()`

![py-shell-exit](../assets/img/py-shell-exit.png)

Note: you can also use the key press ctrl d or ctrl z

--

help is available in interactive mode...

![py-shell-help](../assets/img/py-shell-help.png)

Note: To exit help, type q for "quit" and then hit the enter key. 
You will be taken back to the Python shell

--

you can type simple expressions...

![py-shell-simple](../assets/img/py-shell-simple.png)

Note: check out the big integers in python!!Your calculator will not do this!!

--

secondary prompt for continuation lines...

![py-shell-alt-prompt](../assets/img/py-shell-alt-prompt.png)

Note: you can use tab to indent, and return moves to next line...

---

# iPython

--

documents:

https://ipython.readthedocs.io/en/stable/

Note: I wont cover installing... but if you need help, ask!

--

The iPython shell is much more powerful,

and enables a number of advanced features.

--

in your shell, type `ipython`

![ipython-start](../assets/img/ipython-start.png)

--

to get back to your prompt, type `CTRL-D` or `CTRL-Z`

![ipython-exit](../assets/img/ipython-exit.png)


Note: you can also use the key press ctrl d or ctrl z
Typing an end-of-file character (Control-D on Unix, Control-Z on Windows)
also = to get back to your system prompt, type `exit()` or `quit()`

--

you can type simple expressions...

![ipython-simple](../assets/img/ipython-simple.png)

Note: the prompt is numbered...

--

we get syntax highlighting, and completions

![ipython-complete](../assets/img/ipython-completion.png)

--

we also get tab completion, with object awareness...

![ipython-tab-completion](../assets/img/ipython-tab-completion.png)

Note: here, the interpreter is aware data[0] is a string.

---

# Jupyter

---
