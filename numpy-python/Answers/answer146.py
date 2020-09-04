"""
Problem 146:
The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
"""
from python.utils import rabin_miller
import math


def has_consecutive_prime(s, checks=(1, 3, -5, 7, 9, -11, 13, -17, -19, -21, -23, 27)):
    return not any((not (is_primes := rabin_miller(s + abs(c))) and c > 0) or (c < 0 and is_primes) for c in checks)


def answer(limit=int(1.5e8), div_checks=(3, 7, 9, 13, 27)):
    return sum(int(math.sqrt(s)) for s in map(lambda x: x ** 2, range(10, limit, 10))
               if all(s % d != 0 for d in div_checks) and has_consecutive_prime(s))


if __name__ == '__main__':
    print("Answer is:", answer())




