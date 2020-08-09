"""
Problem 33:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from functools import reduce


def answer():
    return reduce(lambda x, y:  x * y[1] if not y[2] and y[1] <= 9 and print(y) is None else x,
                  ((i / j, *divmod(9 * j * i, 10 * j - i)) for i in range(1, 10) for j in range(1, i)), 1)


if __name__ == '__main__':
    print("Answer is:", answer())

