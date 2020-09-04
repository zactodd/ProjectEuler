"""
Problem 45:

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""


def answer():
    # As Triangle number are a subset of Hexagonal
    p = 165
    h = 143
    h = 84 * p + 97 * h - 38
    return h * (2 * h - 1)


if __name__ == '__main__':
    print("Answer is:", answer())


