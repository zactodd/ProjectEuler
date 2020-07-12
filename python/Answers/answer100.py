"""
Problem 100:
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""
from itertools import count


def answer(limit=10 ** 12):
    d = (3, 4)
    return next((d[0] for _ in count() if (d := (3 * d[0] + 2 * d[1] - 2, 4 * d[0] + 3 * d[1] - 3))[1] > limit), None)


if __name__ == '__main__':
    print("Answer is:", answer())
