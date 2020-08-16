"""
Problem 118:
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
"""

from python.utils import is_prime_list, is_prime, next_permutation
from itertools import repeat, accumulate
PRIMALITY = is_prime_list(10000)


def fast_is_prime(n):
    if n < len(PRIMALITY):
        return PRIMALITY[n]
    else:
        return is_prime(n)


def count_prime_sets(digits, start=0, prev=0):
    if start == len(digits):
        return 1
    else:
        result = 0
        for split in range(start + 1, len(digits) + 1):
            num = int("".join(map(str, digits[start: split])))
            if num > prev and fast_is_prime(num):
                result += count_prime_sets(digits, split, num)
        return result


def answer(digits=list(range(1, 10))):
    return next(s for s in accumulate((count_prime_sets(digits) for _ in repeat(1))) if not next_permutation(digits))


if __name__ == '__main__':
    print("Answer is:", answer())
