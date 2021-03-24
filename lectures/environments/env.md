# Managing the Environment

Dr. David Greenwood

david.greenwood@uea.ac.uk

Room SCI 2.16a

--

## Contents

- Conda Environments
- Pip with Conda
- Python setuptools

--

## Resources

- https://docs.python.org/ 

- https://docs.conda.io/

- https://pypi.org

--

## Motivation

Managing packages and dependencies

Distributing Code

---

## Virtual Environment?

Note: Python applications will often use packages and modules 
that don’t come as part of the standard library. 
Applications will sometimes need a specific version of a library, 
because the application may require that a particular bug has been 
fixed or the application may be written using an obsolete version 
of the library’s interface.

--

## `venv`

Python comes with a module for creating virtual environments.

Note: The venv module provides support for creating lightweight 
virtual environments with their own site directories, 
optionally isolated from system site directories.

--

## `venv`

[venv tutorial](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

Note: 
But, I want to move directly to Conda environments.

---

<!-- .slide: data-auto-animate -->
## Conda Environments

Note: A conda environment is a directory that contains a 
specific collection of conda packages that you have installed.

--

<!-- .slide: data-auto-animate -->
## Conda Environments

`conda` environments go beyond Python modules

Note: Conda is a general-purpose package management system, 
designed to build and manage software of any type from any language. 
As such, it also works well with Python packages.

--

<!-- .slide: data-auto-animate -->
## Conda Environments

```text
conda search --canonical  | grep -v 'py\d\d'
```

the *non* python packages in your environment
<!-- .element: class="fragment" -->

Note: Listing non-Python packages.
This command will list the ones in your environment

--

<!-- .slide: data-auto-animate -->
## Conda Environments

Takes away a lot of the pain!

```text
conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
```

Compare with the `nVidia cuda` install instructions!
<!-- .element: class="fragment" -->

--

<!-- .slide: data-auto-animate -->
## Conda Environments

Create a new environment

`conda create -n myenv python=3.8`

Note: OK, let's look at how to create an environment.

--

<!-- .slide: data-auto-animate -->
## Conda Environments

console will show a *package plan*

Note: you need to accept the plan, and the packages will be downloaded.

--

<!-- .slide: data-auto-animate -->
## Conda Environments

<span style="font-size: 0.7em">

```text [ |9, 10, 12]
The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/osx-64::ca-certificates-2021.1.19-hecd8cb5_1
  certifi            pkgs/main/osx-64::certifi-2020.12.5-py38hecd8cb5_0
  libcxx             pkgs/main/osx-64::libcxx-10.0.0-1
  libffi             pkgs/main/osx-64::libffi-3.3-hb1e8313_2
  ncurses            pkgs/main/osx-64::ncurses-6.2-h0a44026_1
  openssl            pkgs/main/osx-64::openssl-1.1.1j-h9ed2024_0
  pip                pkgs/main/osx-64::pip-21.0.1-py38hecd8cb5_0
  python             pkgs/main/osx-64::python-3.8.8-h88f2d9e_4
  readline           pkgs/main/osx-64::readline-8.1-h9ed2024_0
  setuptools         pkgs/main/osx-64::setuptools-52.0.0-py38hecd8cb5_0
  sqlite             pkgs/main/osx-64::sqlite-3.35.2-hce871da_0
  tk                 pkgs/main/osx-64::tk-8.6.10-hb0a8c7a_0
  wheel              pkgs/main/noarch::wheel-0.36.2-pyhd3eb1b0_0
  xz                 pkgs/main/osx-64::xz-5.2.5-h1de35cc_0
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3

Proceed ([y]/n)? 

```

</span>

Note: there are a few packages installed as well as python itself...
plus some non python items...

--

<!-- .slide: data-auto-animate -->
## Conda Environments

Activate your virtual environment

`conda activate myenv`

or switch between environments
<!-- .element: class="fragment" -->

Note:
to activate or switch into your virtual environment, 
simply type the following where myenv is the name you gave to 
your environment at creation.

--

<!-- .slide: data-auto-animate -->
## Conda Environments

deactivate your virtual environment

`conda deactivate`

Note:
currently active env will be deactivated, 
and the PATH and shell variables will be returned to normal.

--

<!-- .slide: data-auto-animate -->
## Conda Environments

install additional packages

`conda install -n myenv [package]`

failure to specify `-n myenv` will install the package to the root installation
<!-- .element: class="fragment" -->

Note:
to install additional packages only to your virtual environment, 
enter the following command where myenv is the name of your 
environment, and [package] is the name of the package you wish to install. 

Failure to specify `-n myenv` will install the package to the root installation.

--

<!-- .slide: data-auto-animate -->
## Conda Environments

delete an environment

`conda remove -n myenv`

--

<!-- .slide: data-auto-animate -->
## Conda Environments

`environment.yml`

```text
name: stats
dependencies:
  - numpy
  - pandas
```

The first line  sets the new environment name
<!-- .element: class="fragment" -->

Note: For better control, you can create an environment file (environment.yml) manually.
Useful for sharing code.

--

<!-- .slide: data-auto-animate -->
## Conda Environments

`environment.yml`

`conda env create -f environment.yml`

--

<!-- .slide: data-auto-animate -->
## Conda Environments

update `environment.yml`

```text
name: stats
dependencies:
  - numpy
  - pandas
  - nodejs
```

Note: yes, nodejs!

--

<!-- .slide: data-auto-animate -->
## Conda Environments

`conda env update -f environment.yml`

**tip:** you can use update to *create* an environment
<!-- .element: class="fragment" -->

--

<!-- .slide: data-auto-animate -->
## Conda Environments

list all the conda environments available

`conda info --envs`

--

<!-- .slide: data-auto-animate -->
## Conda Environments

save disk space

`conda clean --all`

Note: As you build more projects, each with their own environment, 
you’ll begin to quickly accumulate tarballs from packages you’ve installed.
To get rid of them and free up some disc space, run this.

---

<!-- .slide: data-auto-animate -->
## PIP

--

<!-- .slide: data-auto-animate -->
## PIP

`pip` is the standard package manager for Python

Note: what is pip?
It allows you to install and manage additional packages 
that are not part of the Python standard library. 

--

<!-- .slide: data-auto-animate -->
## PIP

> A tool that allows you to install and manage additional libraries and
> dependencies that are not distributed as part of the standard library.

--

<!-- .slide: data-auto-animate -->
## PIP

Packages are found in the Python Package Index.

### [PyPI](https://pypi.org)
<!-- .element: class="fragment" -->

*pronounced* ` Pie` `Pea` `Eye`
<!-- .element: class="fragment" -->

--

<!-- .slide: data-auto-animate -->
## PIP

`pip install numpy`

Note: I hope you have all seen this somewhere along the way now...

--

<!-- .slide: data-auto-animate -->
## PIP

What about our own packages?

---

<!-- .slide: data-auto-animate -->
## Packaging Python Projects

A good [tutorial](https://python-packaging-tutorial.readthedocs.io)

--

<!-- .slide: data-auto-animate -->
## Packaging Python Projects

### `setuptools` 

**not** part of the standard library
<!-- .element: class="fragment" -->

**will** be available for a `conda` environment
<!-- .element: class="fragment" -->

--

<!-- .slide: data-auto-animate -->
## Packaging Python Projects

```text
git clone https://github.com/davegreenwood/sample-package.git
```

Note: you might have an ssh key installed on github, in which case:
git@github.com:davegreenwood/sample-package.git
or, just download a zip archive.

--

<!-- .slide: data-auto-animate -->
## Packaging Python Projects

<span style="font-size: 1.4em">

```text
├── README.md
├── sample_package
│   └── funcs.py
└── setup.py
```

</span>

--

<!-- .slide: data-auto-animate -->
## Packaging Python Projects

### `setup.py`

```python
from setuptools import setup

setup(
    name="sample",
    description="A simple Python package example.",
    version="0.1",
    author="Dave Greenwood",
    author_email="dave@work.com",
    license="MIT",
    packages=["sample_package"],
)
```

Note: this is an example. 
No arguments are required, but a minimum practical
example would be name and packages...

--

<!-- .slide: data-auto-animate -->
## Packaging Python Projects

`setup.py` allows us to use `pip` to install our own package

--

<!-- .slide: data-auto-animate -->
## Packaging Python Projects

from the parent directory

`pip install .`

Note: pay attention to the full stop (period)
That refers to the current directory.

--

<!-- .slide: data-auto-animate -->
## Packaging Python Projects

allow the package to be editable

`pip install -e .`

Note: this is also called developer mode.

---

## CONDA PIP GIT

making it all work together

--

`git-env.yml`

```yaml
name: git-env
dependencies:
  - python 3.7
  - pip
  - git
  - pip:
    - "git+https://github.com/davegreenwood/sample-package.git"
```

--

let's test in the `python shell`

---

## Summary

- Conda Environments
- Pip
- Python setuptools
- Packaging

--

Slides and code are available on Teams

I have also made everything available on GitHub

--

### [code](https://github.com/uea-teaching/python-introduction)

![qr](../assets/img/ghqr.png)

--

# Questions
