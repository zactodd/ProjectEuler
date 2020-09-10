"""
Problem 145:
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
"""


def answer(limit=9):
    return sum((100 * pow(500, n // 4) if n % 4 == 3 else 0) if n % 2 else 20 * pow(30, n // 2 - 1)
               for n in range(2, limit + 1))


if __name__ == '__main__':
    print("Answer is:", answer())
