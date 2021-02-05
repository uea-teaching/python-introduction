"""Examples for the functions lecture: 
NOTE: This code will not all run, as it includes examples of failure cases.
 """

# %% wrong number of args


def sum_two(a, b):
    print(a + b)


sum_two(3)

# %% unknown args


def print_numbers(*numbers):
    for number in numbers:
        print(number)


print_numbers(1, 2, 3)

# %% keywords


def sum_two(a, b):
    print(a + b)


sum_two(b=3, a=2)

# %% kwargs


def sum_three(**kwargs):
    a = kwargs.get("a")
    b = kwargs.get("b")
    c = kwargs.get("c")
    print(a + b + c)


sum_three(c=3, a=1, b=2)

# %% defaults


def sum_two(a, b=3):
    print(a + b)


sum_two(3)

# %%


def sum_two_or_more(*args, **kwargs):
    print(args[0] + args[1] + kwargs.get("c"))


sum_two_or_more(3, 2, c=4)

# %% fails


def will_break(a, b=3, c):
    print(a+b+c)


will_break(1, 2, 3)

# %% keywords broken


def sum_two(a, b):
    print(a + b)


sum_two(a=2, b)

# %%


def dev_function():
    pass


dev_function()

# %% return


def return_sum_two(a, b):
    return a + b


result = return_sum_two(2, b=3)
print(result)


# %% lambda

def func(a): return a + 10


print(func(5))


# %% lambda

def func(a):
    return a + 10


print(func(5))

# %% lambda real example

data = [("x", 4), ("y", 1), ("z", -5)]
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)

# %%

print(sorted.__doc__)

# %%


def my_function(a, b=5):
    """Return a plus b.

    b is optional, and has a default value of 5.
    """
    return a + b


print(my_function.__doc__)


# %%

def my_function(a, b=5):
    # comments do not become docs...
    pass


print(my_function.__doc__)


# %%

def outer():
    print("I'm the outer function.")

    def inner():
        print("And I'm the inner function.")
    inner()


outer()
# %%


def outer(s):
    print("I'm the outer function.")

    def inner():
        print("The inner function can see the outer data:", s)
    inner()


outer("this is the outer data")


# %%

def num1(x):
    def num2(y):
        return x + y
    return num2


print(num1(10)(5))

# %%


def get_square(val):
    return val ** 2


def get_cube(val):
    return val ** 3


def clickme(val, func):
    return func(val)


print(clickme(5, get_square))
print(clickme(5, get_cube))
