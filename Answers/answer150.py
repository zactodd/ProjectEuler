"""
Problem 150
In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible.

In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of −42.


We wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers sk in the range ±219, using a type of random number generator (known as a Linear Congruential Generator) as follows:

t := 0
for k = 1 up to k = 500500:
    t := (615949*t + 797807) modulo 220
    sk := t−219

Thus: s1 = 273519, s2 = −153582, s3 = 450905 etc

Our triangular array is then formed using the pseudo-random numbers thus:

s1
s2  s3
s4  s5  s6
s7  s8  s9  s10
...
Sub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements directly below it from the next row, the three elements directly below from the row after that, and so on).
The "sum of a sub-triangle" is defined as the sum of all the elements it contains.
Find the smallest possible sub-triangle sum.
"""
import numpy as np


def lcg_random():
    state = 0
    while True:
        state = (615949 * state + 797807) & ((1 << 20) - 1)
        yield state - (1 << 19)


def answer():
    r = 1000
    rand = lcg_random()
    triangle = [[next(rand) for j in range(i + 1)] for i in range(r)]

    r = len(triangle)
    row_sums = np.zeros([r, r + 2], dtype=np.int64)
    for (i, row) in enumerate(triangle):
        row_sums[i, :i + 2] = np.cumsum([0] + row, dtype=np.int64)
    m = 0
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            ks = np.arange(i, r, dtype=np.uint32)
            terms = row_sums[ks, ks - i + 1 + j] - row_sums[ks, j]
            sums = np.cumsum(terms, dtype=np.int64)
            m = min(np.min(sums), m)
    return m


if __name__ == '__main__':
    print("Answer is:", answer())
