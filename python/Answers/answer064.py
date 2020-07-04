"""
Problem 64:
All square roots are periodic when written as continued fractions and can be written in the form:

N−−√=a0+1a1+1a2+1a3+…
For example, let us consider 23−−√:23−−√=4+23−−√−4=4+1123√−4=4+11+23√−37
If we continue we would get the following expansion:

23−−√=4+11+13+11+18+…
The process can be summarised as follows:

a0=4,123√−4=23√+47=1+23√−37
a1=1,723√−3=7(23√+3)14=3+23√−32
a2=3,223√−3=2(23√+3)14=1+23√−47
a3=1,723√−4=7(23√+4)7=8+23−−√−4
a4=8,123√−4=23√+47=1+23√−37
a5=1,723√−3=7(23√+3)14=3+23√−32
a6=3,223√−3=2(23√+3)14=1+23√−47
a7=1,723√−4=7(23√+4)7=8+23−−√−4
It can be seen that the sequence is repeating. For conciseness, we use the notation 23−−√=[4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

2–√=[1;(2)], period=1
3–√=[1;(1,2)], period=2
5–√=[2;(4)], period=1
6–√=[2;(2,4)], period=2
7–√=[2;(1,1,1,4)], period=4
8–√=[2;(1,4)], period=2
10−−√=[3;(6)], period=1
11−−√=[3;(3,6)], period=2
12−−√=[3;(2,6)], period=2
13−−√=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N≤13, have an odd period.

How many continued fractions for N≤10000 have an odd period?
"""

from math import sqrt


def answer():
    n, odd_period = 10000, 0
    for i in range(2, n + 1):
        r = limit = int(sqrt(i))
        if limit ** 2 == i:
            continue

        k, period = 1, 0
        while k != 1 or period == 0:
            period += 1
            k = (i - r * r) // k
            r = (limit + r) // k * k - r
        if period % 2 == 1:
            odd_period += 1
    return odd_period


if __name__ == '__main__':
    print("Answer is:", answer())
