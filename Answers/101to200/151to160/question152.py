"""
Question 152:
There are several ways to write the number 1/2 as a sum of inverse squares using distinct integers.

For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:

12=122+132+142+152+172+1122+1152+1202+1282+1352
In fact, only using integers between 2 and 45 inclusive, there are exactly three ways to do it, the remaining two being: {2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.

How many ways are there to write the number 1/2 as a sum of inverse squares using distinct integers between 2 and 80 inclusive?
"""


from fractions import Fraction
from itertools import combinations
from utils import fast_primes


def subsets(u):
    universal_size = len(u)
    for subset_size in range(universal_size + 1):
        for subset in combinations(u, subset_size):
            yield subset


def sum_and_frequency(elements):
    s = 0
    frequency = 1
    for e, f in elements:
        s += e
        frequency *= f
    return s, frequency


def primes_largest_divisors(n):
    output = [None for i in range(n + 1)]
    visited = [False for i in range(n + 1)]
    visited[0] = visited[1] = True
    for i in range(2, n + 1):
        if not visited[i]:
            for j in range(i, n + 1, i):
                output[j] = i
                visited[j] = True
    return output


def largest_prime_divisor(n, primes):
    for prime in primes:
        if n % prime == 0:
            return prime
    return 1


def answer():
    n = 80
    primes = list(fast_primes(n // 2))[::-1]
    prime_divisors = primes_largest_divisors(n)

    def next_restricted_element(fes, res, largest_prime):
        elements = {}
        for rs, rf in res:
            for e in subsets(fes):
                fs, ff = sum_and_frequency(e)
                s, f = rs + fs, rf * ff
                lpd = largest_prime_divisor(s.denominator, primes)
                if largest_prime == 2 or lpd < largest_prime:
                    if s not in elements:
                        elements[s] = 0
                    elements[s] += f
        return list(elements.items())

    free_elements = {}
    for i in range(2, n + 1):
        divisor = prime_divisors[i]
        if divisor not in free_elements:
            free_elements[divisor] = []
        free_elements[divisor].append((Fraction(1, i ** 2), 1))

    prime, *rest = primes
    restricted_elements = next_restricted_element(free_elements[prime], [(0, 1)], prime)
    for prime in rest:
        restricted_elements = next_restricted_element(free_elements[prime], restricted_elements, prime)

    for s, f in restricted_elements:
        if s == Fraction(1, 2):
            return f
    return None


if __name__ == '__main__':
    print("Answer is:", answer())
