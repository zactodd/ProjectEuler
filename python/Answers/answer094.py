"""
Problem 94:
It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""


def answer(limit = 10 ** 9):
    s0, s1, s, p, m = 1, 1, 0, 0, 1
    while p <= limit:
        s0, s1, m = s1, 4 * s1 - s0 + 2 * m, -m
        s += p
        p = 3 * s1 - m
    return s


if __name__ == '__main__':
    print("Answer is:", answer())
