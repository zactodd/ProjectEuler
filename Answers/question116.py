"""
Question 116:
A row of five grey square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

png116_1.png
If green tiles are chosen there are three ways.

png116_2.png
And if blue tiles are chosen there are two ways.

png116_3.png
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the grey tiles in a row measuring five units in length.

How many different ways can the grey tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

NOTE: This is related to Problem 117.
"""


def f(m, n):
    ways = [1] * m + [0] * (n-m+1)
    for j in range(m, n+1):
        ways[j] += ways[j - 1] + ways[j - m]
    return ways[n] - 1


def answer():
    n = 50
    return f(2, n) + f(3, n) + f(4, n)


if __name__ == '__main__':
    print("Answer is:", answer())
