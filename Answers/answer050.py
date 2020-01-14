"""
Problem 50:
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from utils import fast_primes


def answer():
    limit = 1000000
    primes = fast_primes(limit)
    prime_sum = [0]
    for p in primes:
        prime_sum.append(prime_sum[-1] + p)
        if prime_sum[-1] >= limit:
            break
    c = len(prime_sum)

    consec = 1
    for i in range(c):
        for j in range(c - 1, i + consec, -1):
            n = prime_sum[j] - prime_sum[i]
            if j - i > consec and n in primes:
                consec, max_prime = j - i, n
                break
    return max_prime


if __name__ == '__main__':
    print("Answer is:", answer())

