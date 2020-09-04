"""
Problem 144
In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam. The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation 4x2 + y2 = 100

The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light to enter and exit through the hole.


The light beam in this problem starts at the point (0.0,10.1) just outside the white cell, and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection "angle of incidence equals angle of reflection." That is, both the incident and reflected beams make the same angle with the normal line at the point of incidence.

In the figure on the left, the red line shows the first two points of contact between the laser beam and the wall of the white cell; the blue line shows the line tangent to the ellipse at the point of incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is: m = −4x/y

The normal line is perpendicular to this tangent line at the point of incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?
"""
import math
from itertools import repeat, accumulate


def quad_roots(a, b, c):
    return (-b - (d := math.sqrt(b * b - 4 * a * c))) / (a2 := (2 * a)), (-b + d) / a2


def update_beam(xa, ya, xo, yo):
    slope_a = (yo - ya) / (xo - xa)
    slope_o = -4 * xo / yo
    tan_a = (slope_a - slope_o) / (1 + slope_a * slope_o)
    slope_b = (slope_o - tan_a) / (1 + tan_a * slope_o)
    intercept_b = yo - slope_b * xo

    r1, r2 = quad_roots(4 + slope_b ** 2, 2 * slope_b * intercept_b, intercept_b ** 2 - 100)

    xa, ya = xo, yo
    xo = r1 if (abs(r1 - xo) > abs(r2 - xo)) else r2
    yo = slope_b * xo + intercept_b
    return xa, ya, xo, yo


def answer(xa=0.0, ya=10.1, xo=1.4, yo=-9.6):
    return next(i for i, p in enumerate(accumulate(repeat(1), lambda p, _: update_beam(*p), initial=(xa, ya, xo, yo)))
                if 0.01 >= p[2] >= -0.01 and p[3] >= 0)


if __name__ == '__main__':
    print("Answer is:", answer())
