"""
Question 165:
A segment is uniquely defined by its two endpoints.
By considering two line segments in plane geometry there are three possibilities:
the segments have zero points, one point, or infinitely many points in common.

Moreover when two segments have exactly one point in common it might be the case that that common point is an endpoint of either one of the segments or of both. If a common point of two segments is not an endpoint of either of the segments it is an interior point of both segments.
We will call a common point T of two segments L1 and L2 a true intersection point of L1 and L2 if T is the only common point of L1 and L2 and T is an interior point of both segments.

Consider the three segments L1, L2, and L3:

L1: (27, 44) to (12, 32)
L2: (46, 53) to (17, 62)
L3: (46, 70) to (22, 40)

It can be verified that line segments L2 and L3 have a true intersection point. We note that as the one of the end points of L3: (22,40) lies on L1 this is not considered to be a true point of intersection. L1 and L2 have no common point. So among the three line segments, we find one true intersection point.

Now let us do the same for 5000 line segments. To this end, we generate 20000 numbers using the so-called "Blum Blum Shub" pseudo-random number generator.

s0 = 290797

sn+1 = sn×sn (modulo 50515093)

tn = sn (modulo 500)

To create each line segment, we use four consecutive numbers tn. That is, the first line segment is given by:

(t1, t2) to (t3, t4)

The first four numbers computed according to the above generator should be: 27, 144, 12 and 232. The first segment would thus be (27,144) to (12,232).

How many distinct true intersection points are found among the 5000 line segments?
"""


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])


def solve(p1, p2, p3, p4):
    if cross(p1, p2, p3) * cross(p1, p2, p4) < 0 and cross(p3, p4, p1) * cross(p3, p4, p2) < 0:
        pa, pb, pc = p1[1] - p2[1], p2[0] - p1[0], p1[0] * p2[1] - p2[0] * p1[1]
        qa, qb, qc = p3[1] - p4[1], p4[0] - p3[0], p3[0] * p4[1] - p4[0] * p3[1]
        xa, xb, xc = pb * qc - qb * pc, pc * qa - qc * pa, pa * qb - qa * pb
        return xa / xc, xb / xc
    else:
        return -1, -1


def answer():
    n = 5000
    s = [0] * n * 400
    p = [0] * n * 400
    s[0] = 290797
    for i in range(n * 4):
        s[i + 1] = s[i] * s[i] % 50515093
    for i in range(n * 2 + 1):
        p[i] = s[2 * i - 1] % 500, s[2 * i - 0] % 500
    pairs = set()
    for i in range(n):
        for j in range(i + 1, n):
            pairs.add(solve(p[i * 2 + 1], p[i * 2 + 2], p[j * 2 + 1], p[j * 2 + 2]))
    return len(pairs) - 1


if __name__ == '__main__':
    print("Answer is:", answer())
