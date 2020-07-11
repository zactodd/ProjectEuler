"""
Problem 30:
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

from itertools import combinations_with_replacement


def answer(n=5):
    p = {str(i): i ** n for i in range(10)}
    if n <= 5:
        n += 1
    return sum(t for i in combinations_with_replacement("0123456789", n)
               if (t := sum(p[x] for x in i)) == sum(p[x] for x in str(t)) and t > 9)


if __name__ == '__main__':
    print("Answer is:", answer())
