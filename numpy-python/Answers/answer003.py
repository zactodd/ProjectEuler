"""
Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from python.utils import factors


def answer(n=600851475143):
    return factors(n)


if __name__ == '__main__':
    print("Answer is:", answer())
