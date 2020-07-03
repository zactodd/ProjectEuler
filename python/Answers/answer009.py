"""
Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def answer():
    n = 1000
    return next((a * b * c for a in range(1, n + 1) for b in range(a + 1, n + 1)
                 if a * a + b * b == (c := (n - a - b)) ** 2), None)


if __name__ == '__main__':
    print("Answer is:", answer())
