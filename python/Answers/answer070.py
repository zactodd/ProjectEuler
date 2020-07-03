"""
Problem 70:
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

from python.utils import totients, is_perm


def answer():
    ts = totients(10 ** 7)
    m, n = 1, 0
    for i, t in enumerate(ts[2:], 2):
        if i * n < m * t and is_perm(i, t):
            m, n = i, ts[i]
    return m


if __name__ == '__main__':
    print("Answer is:", answer())
