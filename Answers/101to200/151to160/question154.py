"""
Question 154:
A triangular pyramid is constructed using spherical balls so that each ball rests on exactly three balls of the next lower level.


Then, we calculate the number of paths leading from the apex to each position:

A path starts at the apex and progresses downwards to any of the three spheres directly below the current position.

Consequently, the number of paths to reach a certain position is the sum of the numbers immediately above it (depending on the position, there are up to three numbers above it).

The result is Pascal's pyramid and the numbers at each level n are the coefficients of the trinomial expansion (x + y + z)n.

How many coefficients in the expansion of (x + y + z)200000 are multiples of 1012?
"""


def make_pool(n, p):
    pool = [0] * (n + 1)
    for i in range(1, n + 1):
        ii = i // p
        pool[i] = ii + pool[ii]
    return pool


def answer():
    m, limit = 200000, 12
    p2, p5 = make_pool(m, 2), make_pool(m, 5)
    m2, m5 = p2[m] - limit, p5[m] - limit
    count = 0
    for a in range(m, (m - 1) // 3, -1):
        a5, a2 = m5 - p5[a], m2 - p2[a]
        for b in range((m - a + 1) // 2, min(a, m - a) + 1):
            c = m - a - b
            if p5[b] + p5[c] <= a5 and p2[b] + p2[c] <= a2:
                count += 6 if a != b != c else 3
    return count


if __name__ == '__main__':
    print("Answer is:", answer())
