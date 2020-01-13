"""
Question 131:
There are some prime values, p, for which there exists a positive integer, n, such that the expression n3 + n2p is a perfect cube.

For example, when p = 19, 83 + 82×19 = 123.

What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
"""
from utils import fast_primes
import math


def answer():
    m = 10 ** 6
    primes = fast_primes(m)
    m = int(math.sqrt(m / 3))
    return len(set(3 * x * x + 3 * x + 1 for x in range(m)).intersection(primes))


if __name__ == '__main__':
    print("Answer is:", answer())
