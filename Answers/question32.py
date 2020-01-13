"""
Question 32:

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from itertools import permutations


def answer():
    s = 0
    prods = set()
    for i in permutations("123456789*=", 11):
        if (star := i.index("*")) > (equals := i.index("=")) or abs(star - equals) == 1:
            continue
        # elif star == 1:
        #     break
        n, m, p = i[:star], i[star + 1:equals], i[equals + 1:]
        if len(p) < len(n) or len(p) < len(m) or len(n) == 0 or len(m) == 0:
            continue
        elif int("".join(n)) * int("".join(m)) == (prod := int("".join(p))):
            prods.add(prod)
    return sum(prods)


if __name__ == '__main__':
    print("Answer is:", answer())
