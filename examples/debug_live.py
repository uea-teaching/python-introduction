"""just for testing an interactive debugger"""

def foo(a, b):
    c = a + b
    return c


def bar(a, b, c):
    d = a + b * c
    return d


def foobar(a, b):
    result = []
    for i in [1, 2, 3]:
        for j in [1, 2]:
            x = foo(i, j)
            y = bar(x, a, b)
            result.append([x, y])
    return True


if __name__ == "__main__":
   foobar(1, 2)
