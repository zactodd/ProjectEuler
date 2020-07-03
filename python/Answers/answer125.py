"""
Problem 125:
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.
"""


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def answer():
    limit = 10 ** 8
    sq_limit = int(10 ** 4)
    pal = set()
    for i in range(1, sq_limit):
        s = i ** 2
        while s < limit:
            i += 1
            s += i ** 2
            if is_palindrome(s):
                pal.add(s)
    return sum(pal)


if __name__ == '__main__':
    print("Answer is:", answer())
