"""
Question 51:
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

from utils import fast_primes, is_prime


def eight_primes(prime, rd):
    return sum((n := int(str(prime).replace(rd, d))) > 100000 and is_prime(n) for d in "0123456789") == 8


def answer():
    for prime in fast_primes(1000000):
        if prime > 100000:
            str_prime = str(prime)
            last_digit = str_prime[5:6]
            if (str_prime.count('0') == 3 and eight_primes(str_prime, '0') or
                    str_prime.count('1') == 3 and last_digit != '1' and eight_primes(str_prime, '1') or
                    str_prime.count('2') == 3 and eight_primes(str_prime, '2')):
                return int(str_prime)
    return None


if __name__ == '__main__':
    print("Answer is:", answer())
