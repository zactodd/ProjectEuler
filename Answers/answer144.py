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


def quad_roots(a, b, c):
    disc_o2a = math.sqrt(b * b - 4 * a * c) / (2 * a)
    return -b - disc_o2a, -b + disc_o2a


def answer():
    x_a, y_a, x_o, y_o  = 0.0, 10.1, 1.4, -9.6
    count = 0
    while x_o > 0.01 or x_o < -0.01 or y_o < 0:
        slope_a = (y_o - y_a) / (x_o - x_a)
        slope_o = -4 * x_o / y_o
        tan_a = (slope_a - slope_o) / (1 + slope_a * slope_o)
        slope_b = (slope_o - tan_a) / (1 + tan_a * slope_o)
        intercept_b = y_o - slope_b * x_o

        a = 4 + slope_b ** 2
        b = 2 * slope_b * intercept_b
        c = intercept_b ** 2 - 100

        r1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        r2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)

        x_a = x_o
        y_a = y_o

        x_o = r1 if (abs(r1 - x_o) > abs(r2 - x_o)) else r2
        y_o = slope_b * x_o + intercept_b
        count += 1
    return count


if __name__ == '__main__':
    print("Answer is:", answer())
