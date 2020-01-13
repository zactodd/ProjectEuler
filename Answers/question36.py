"""
Question 36:

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from utils import is_palindrome, bin_as_10


def answer():
    n = int(1e6)
    return sum(i for i in range(1, n) if is_palindrome(i) and is_palindrome(bin_as_10(i)))


if __name__ == '__main__':
    print("Answer is:", answer())
