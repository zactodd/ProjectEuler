"""
Question 99:
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
from math import log
BASE_EXP_FILE = "../../../resources/base_exp.txt"
with open(BASE_EXP_FILE, "r") as f:
    PAIRS = [tuple(map(int, line.split(","))) for line in f.readlines()]


def answer():
    return max(enumerate(PAIRS), key=lambda x: x[1][1] * log(x[1][0]))[0] + 1


if __name__ == '__main__':
    print("Answer is:", answer())
