"""
Problem 86:
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
"""
import math


def answer():
    limit, c, a = int(1e6), 0, 2
    while c < limit:
        a += 1
        c += sum(min(bc, a + 1) - (bc + 1) // 2 for bc in range(3, 2 * a)
                 if (bc * a) % 12 == 0 and not math.sqrt(bc * bc + a * a) % 1)
    return a


if __name__ == '__main__':
    print("Answer is:", answer())
