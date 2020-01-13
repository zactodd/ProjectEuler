"""
Question 146:
The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
"""
from utils import fast_primes
import math

INCREMENTS = [1, 3, 7, 9, 13, 27]  # Must be in non-decreasing order
NON_INCREMENTS = set(range(INCREMENTS[-1])) - set(INCREMENTS)


def answer():
    limit = 150000000

    max_num = limit ** 2 + INCREMENTS[-1]
    primes = fast_primes(int(math.sqrt(max_num)))

    def has_consecutive(n):
        n2 = n ** 2
        if any((x != p and x % p == 0) for p in primes for x in [(n2 + k) for k in INCREMENTS]):
            return False
        return all((not is_prime(n2 + k)) for k in NON_INCREMENTS)

    def is_prime(n):
        end = math.sqrt(n)
        for p in primes:
            if p > end:
                break
            if n % p == 0:
                return False
        return True

    return sum(n for n in range(0, limit, 10) if has_consecutive(n))


if __name__ == '__main__':
    print("Answer is:", answer())
