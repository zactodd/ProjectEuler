"""
Problem 34:

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial
DIGIT_FACTS = [factorial(d) for d in range(10)]


def answer(limit=int(1e5)):
    return sum(i for i in range(10, limit) if i == sum(DIGIT_FACTS[int(j)] for j in str(i)))


if __name__ == '__main__':
    print("Answer is:", answer())
