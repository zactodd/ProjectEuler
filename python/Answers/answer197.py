"""

"""

import math
from functools import reduce


def f(x, depths=1):
    return reduce(lambda i, _: math.floor(2.0 ** (30.403243784 - i * i)) / 1.0e9, range(depths), x)


def answer(l=10 ** 12):
    x, y = f(-1), f(f(-1))
    i, x, y = next((i, a, b) for i, a, b in map(lambda n: (n, f(x), f(y, 2)), range(1, l)) if (x := a) == (y := b))
    return math.floor(((x := f(x, (l - i) % i)) + f(x)) * 1.0e9) / 1.0e9


if __name__ == "__main__":
    print("Answer is:", answer())
