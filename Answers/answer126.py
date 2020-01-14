"""
Problem 126:
The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.


If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.

However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.

It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.
"""


def answer():
    n = 1000
    m = 20000

    cubes = [0] * m
    for a in range(1, m):
        for b in range(1, a + 1):
            if a * b * 2 >= m:
                break
            for c in range(1, b + 1):
                if (s := ((a + b) * c + a * b) * 2) >= m:
                    break
                ss = 4 * (a + b + c)
                cubes[s] += 1
                for k in range(0, m, 8):
                    s += ss + k
                    if s >= m:
                        break
                    cubes[s] += 1
    return cubes.index(n)


if __name__ == '__main__':
    print("Answer is:", answer())

