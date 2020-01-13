"""
Question 85:
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""

from math import sqrt


def answer():
    limit, x, min_diff = 2000000, 2, float('Inf')
    y = limit // 6
    area = None
    while x <= y:
        d = abs(x * (x + 1) * y * (y + 1) // 4 - limit)
        if d < min_diff:
            area, min_diff, xx, yy = x * y, d, x, y
        x += 2
        y = int(sqrt(limit * 4 / (x * x + x)))
    return area


if __name__ == '__main__':
    print("Answer is:", answer())

