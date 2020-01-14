"""
Problem 142:
Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
"""
from itertools import count
from utils import is_perfect_square


def answer():
    for i in count(4):
        a = i ** 2
        for j in range(3, i):
            c = j ** 2
            f = a - c
            if f <= 0 or not is_perfect_square(f):
                continue
            for k in range(1 if j % 2 == 1 else 2, j, 2):
                e = a - k ** 2
                b = c - e
                if b <= 0 or e <= 0 or not is_perfect_square(b) or not is_perfect_square(e):
                    continue
                return (2 * c + e + f) // 2
    return None


if __name__ == '__main__':
    print("Answer is:", answer())
