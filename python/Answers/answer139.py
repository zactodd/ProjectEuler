"""
Problem 139:
Let (a, b, c) represent the three sides of a right angle triangle with integral length sides. It is possible to place four such triangles together to form a square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5 square can be tiled with twenty-five 1 by 1 squares.


However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7 and these could not be used to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred million, how many Pythagorean triangles would allow such a tiling to take place?
"""
from itertools import accumulate, takewhile, repeat


def answer(limit=int(1e8)):
    return sum((limit - 1) // (x + y) for x, y in
               takewhile(lambda j: sum(j) <= limit,
                         accumulate(repeat(1), lambda i, _: (3 * i[0] + 4 * i[1], 2 * i[0] + 3 * i[1]),
                                    initial=(7, 5))))


if __name__ == '__main__':
    print("Answer is:", answer())
