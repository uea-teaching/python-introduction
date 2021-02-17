# Introduction to Programming with Python

This module introduces the programming language Python, 
for students with little or no previous programming experience.


## Lectures

The material is presented as a series of lectures and some code examples.

The online lectures are available [here](https://uea-teaching.github.io/python-introduction/).

I will make the slides available online *and* I will try to keep this material low-bandwidth.


## Requirements

This course covers the Python programming language. 
Regardless of the platform you are working on, Python is available.

The only requirement to view the slides is a web browser - with javascript enabled. 
For very low bandwidth users, you can view the raw text files for each lecture
by navigating [here](https://github.com/uea-teaching/python-introduction/).


## Viewing offline

If you want to view the slides offline, 
clone this repository and cd to the lectures directory.

Run a local http server:

    python -m http.server

The slides can then be viewed at `http://localhost:8000`


## PDF

I discourage printing of the slides. 
If you want a static pdf version of the slides I recommend, 
and use, [decktape](https://github.com/astefanutti/decktape).

> I also recommend using the docker image provided at the link.

For example, to generate a pdf file of the collections lecture:

    decktape reveal  \
        --size 1280x960 \
        https://uea-teaching.github.io/python-introduction/lectures/collections \
        collections.pdf
