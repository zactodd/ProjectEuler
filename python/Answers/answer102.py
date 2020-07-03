"""
Problem 102:
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.


"""

TRIANGLES_FILE = "../../resources/triangles.txt"
with open(TRIANGLES_FILE, "r") as f:
    TRIANGLES = [list(map(int, line.split(","))) for line in f.readlines()]


def sgn(x):
    return (x > 0) - (x < 0)


def is_origin(x0, y0, x1, y1, x2, y2):
    o = sgn((y0 - y1) * x0 - (x0 - x1) * y0), sgn((y1 - y2) * x1 - (x1 - x2) * y1), sgn((y2 - y0) * x2 - (x2 - x0) * y2)
    return 0 in o or len(set(o)) == 1


def answer():
    return sum(is_origin(*c) for c in TRIANGLES)


if __name__ == '__main__':
    print("Answer is:", answer())

