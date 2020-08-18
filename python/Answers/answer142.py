"""
Problem 142:
Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
"""
from itertools import count
from python.utils import is_perfect_square


def answer():
    return next((c + e + a) // 2 for i, a in map(lambda x: (x, x ** 2), count(4))
                for j, c in filter(lambda x: is_perfect_square(a - x[1]), map(lambda x: (x, x ** 2), range(3, i)))
                for k in range(1 if j % 2 == 1 else 2, j, 2)
                if (e := a - k ** 2) > 0 and (b := c - e) > 0 and is_perfect_square(e) and is_perfect_square(b))


if __name__ == '__main__':
    print("Answer is:", answer())
