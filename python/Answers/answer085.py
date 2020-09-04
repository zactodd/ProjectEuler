"""
Problem 85:
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""

from math import sqrt
from itertools import count


def answer(limit=2000000):
    min_diff, area = float("Inf"), None
    for x, y in map(lambda c: (c, int(sqrt(limit * 4 / (c * c + c)))), count(2, 2)):
        if x > y:
            return area
        elif (d := (abs(x * (x + 1) * y * (y + 1) // 4 - limit))) < min_diff:
            area, min_diff, xx, yy = x * y, d, x, y


if __name__ == '__main__':
    print("Answer is:", answer())

