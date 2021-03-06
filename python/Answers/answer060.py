"""
Problem 60:
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from python.utils import fast_primes, is_prime
from itertools import permutations, repeat


def make_chain(primes, chain, size):
    if len(chain) == size:
        return chain
    elif any((new_chain := make_chain(primes, chain + [p], size)) for p in primes
             if p > chain[-1] and all_prime(chain + [p])):
        return new_chain
    else:
        return False


def all_prime(chain):
    return all(is_prime(int(str(p1) + str(p2))) for p1, p2 in permutations(chain, 2))


def answer(limit=10000, n=5):
    primes = list(fast_primes(limit))
    return sum(map(int, next((c for _ in repeat(1) if (c := make_chain(primes, [primes.pop(0)], n))))))


if __name__ == '__main__':
    print("Answer is:", answer())
