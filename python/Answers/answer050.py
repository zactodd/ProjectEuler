"""
Problem 50:
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from python.utils import fast_primes
from functools import reduce
from itertools import accumulate, takewhile


def answer(limit=1000000):
    p_acc = list(takewhile(lambda p: p < limit, accumulate(primes := fast_primes(limit))))
    return reduce(lambda x, y: next(
            ((j - y, n) for j in range(c - 1, y + x[0], -1) if j - y > x[0] and (n := p_acc[j] - p_acc[y]) in primes),
            x
        ), range(c := len(p_acc)), (1, 0))[1]


if __name__ == '__main__':
    print("Answer is:", answer())

